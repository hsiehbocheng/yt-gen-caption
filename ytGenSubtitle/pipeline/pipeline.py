from .steps.step import StepException
# why importError when from steps.step import StepException


class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, input_kwargs):
        for step in self.steps:
            try:
                step.process(input_kwargs)
            except:
                print("Error occurred in step: ", step)
                break
