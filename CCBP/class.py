class Mobile:
    def __init__(self, model, camera):
        self.model = model
        self.camera = camera


    def make_call(self, number):
        print(f" calling....{number}")

    def update_model(self, model):
        self.model = model

    def get_model(self):
        print(self.model)

mobile_obj = Mobile("Galaxy j2",  "32 MP")
mobile_obj.make_call(48585546)
mobile_obj.get_model()
mobile_obj.update_model("VIVO_y31")
mobile_obj.get_model()

# print()
# mobile_obj1 = Mobile("Galaxy j2",  "32 MP")
# mobile_obj1.make_call(48585546)
# print(id(mobile_obj1))