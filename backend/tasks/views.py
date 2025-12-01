from rest_framework.response import Response
from rest_framework.views import APIView
from .scoring import calculate_priority

class AnalyzeTasks(APIView):
    def post(self, request):
        tasks = request.data
        for task in tasks:
            task["score"] = calculate_priority(task)
            task["explanation"] = "Priority calculated based on urgency, importance, effort, and dependencies."
        tasks = sorted(tasks, key=lambda x: x["score"], reverse=True)
        return Response(tasks)

class SuggestTasks(APIView):
    def get(self, request):
        # Simulated fetch (in real world pull from DB)
        tasks = []  # placeholder
        top = sorted(tasks, key=lambda x: x["score"], reverse=True)[:3]
        return Response(top)
