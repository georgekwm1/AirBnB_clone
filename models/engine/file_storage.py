from models.base_model import BaseModel
import json

class FileStorage():
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects.items()
    
    def new(self, obj):
        class_name = obj.__class__.__name__
        FileStorage.__objects.append(f"{class_name}.{obj.id}")

    def save(self):
        my_string = json.dumps(self.__objects)
        with open(FileStorage.__file_path, 'w') as file:
            file.write(my_string)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                json_string = file.read()
            FileStorage.__objects = json.loads(json_string)

        except FileNotFoundError:
            pass 