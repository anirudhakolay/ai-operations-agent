def run_agent(task: str):
    task_lower = task.lower()

    try:
        # calculate expression
        if task_lower.startswith("calculate"):
            expr = task_lower.replace("calculate", "").strip()
            return eval(expr)

        # add
        elif task_lower.startswith("add"):
            nums = [int(s) for s in task_lower.split() if s.isdigit()]
            return sum(nums)

        # subtract
        elif task_lower.startswith("subtract"):
            nums = [int(s) for s in task_lower.split() if s.isdigit()]
            return nums[1] - nums[0]

        # multiply
        elif task_lower.startswith("multiply"):
            nums = [int(s) for s in task_lower.split() if s.isdigit()]
            result = 1
            for n in nums:
                result *= n
            return result

        # divide
        elif task_lower.startswith("divide"):
            nums = [int(s) for s in task_lower.split() if s.isdigit()]
            return nums[0] / nums[1]

        else:
            return "I cannot handle this task yet"

    except Exception as e:
        return f"Error: {str(e)}"

# import requests

# def get_weather(city: str):
#     url = f"https://api.open-meteo.com/v1/forecast?latitude=19.07&longitude=72.87&current_weather=true"
#     response = requests.get(url)
#     return response.json()["current_weather"]
