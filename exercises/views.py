import random

from django.shortcuts import get_object_or_404, render, redirect
from django.views import View

from exercises.forms import AnswerForm
from exercises.models import OperationChoices
from players.models import Player, Score


class GameView(View):
    def get_numbers(self, operation):
        op = str(operation).upper()
        if op == 'ADD':
            n1, n2 = random.randint(0, 10), random.randint(0, 10)
            return n1, n2, n1 + n2, '+'
        elif op == 'SUBTRACT':
            n1, n2 = random.randint(0, 10), random.randint(0, 10)
            if n1 < n2: n1, n2 = n2, n1
            return n1, n2, n1 - n2, '-'
        elif op == 'MULTIPLY':
            n1, n2 = random.randint(1, 10), random.randint(1, 10)
            return n1, n2, n1 * n2, '*'
        elif op == 'DIVIDE':
            n1, n2 = random.randint(1, 10), random.randint(1, 10)
            while n1 % n2 != 0:
                n1, n2 = random.randint(1, 10), random.randint(1, 10)
            return n1, n2, n1 // n2, '/'

        return 0, 0, 0, '?'

    def get(self, request, child_id, operation):
        if 'question_count' not in request.session:
            request.session['question_count'] = 1
        child = get_object_or_404(Player, id=child_id)
        n1, n2, correct_answer, symbol = self.get_numbers(operation)
        request.session['correct_answer'] = correct_answer
        template_name = 'play.html'

        context = {
            'child': child,
            'num1': n1,
            'num2': n2,
            'symbol': symbol,
            'form': AnswerForm(),
            'operation': operation.upper()
        }
        return render(request, template_name, context)

    def post(self, request, child_id, operation):
        child = get_object_or_404(Player, id=child_id)
        form = AnswerForm(request.POST)
        correct_answer = request.session.get('correct_answer')
        current_count = request.session.get('question_count', 1)
        request.session['question_count'] = current_count + 1
        if current_count == 10:
            del request.session['question_count']
            return render(request, 'final_score.html', {'child': child,
                                                        'operation': operation,
                                                        'message': "Game Over! You finished 10 questions!"})
        if form.is_valid():
            user_answer = form.cleaned_data['user_answer']

            if user_answer == correct_answer:
                Score.objects.create(player=child, score=10, operation_type=operation)
                message = "Gooood Job"
                is_correct = True
            else:
                message = f"Oooops, wrong answer. The right answer was {correct_answer}."
                is_correct = False

            return render(request, 'result.html', {
                'child': child,
                'is_correct': is_correct,
                'message': message,
                'operation': operation,
                'correct_answer': correct_answer
            })
        if correct_answer is None:
            return redirect('play_game', child_id=child.id, operation=operation)

        return render(request, f'operations/{operation.lower()}.html', context={
            'form': form,
            'child': child
        })

def MathMenuView(request, child_id):
    from players.models import Player
    from django.shortcuts import render, get_object_or_404

    child = get_object_or_404(Player, id=child_id)
    return render(request, 'math_operations.html', {
        'child': child
})

