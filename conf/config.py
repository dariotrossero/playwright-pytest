class Config:

    properties = {}

    @classmethod
    def load_properties(cls):
        with open("conf/secrets.env") as f:
            lines = f.readlines()
            for line in lines:
                key, value = line.split("=")
                cls.properties[key] = value

    @classmethod
    def show_values(cls):
        return cls.properties
