from .steps.step import StepException
# why importError when from steps.step import StepException


class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, input_kwargs):
        temp_data = None
        for step in self.steps:
            temp_data = step.process(input_kwargs, temp_data)

            # try:
            #     temp_data = step.process(input_kwargs, temp_data)
            # except:
            #     print("Error occurred in step: ", step)
            #     break
