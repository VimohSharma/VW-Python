import time
from abc import ABC, abstractmethod

def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"log executing {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def measure_time(func):
    def wrapper(*args, **kwargs):
        start=time.time()
        res=func(*args, **kwargs)
        end=time.time()
        print(f"time {func.__name__} took {end-start:.4f} seconds.")
        return res
    return wrapper

class FileManage:
    def __init__(self,filename):
        self.filename = filename
        self.file=None

    def __enter__(self):
        self.file=open(self.filename, "w")
        print("FILE OPENED")
        return self.file
    
    def __exit__(self,exc_type,exc_val,exc_tb):
        self.file.close()
        print("CLOSING FILE")

class Report(ABC):

    @abstractmethod
    def generate_date(self):
        pass

    @log_execution
    @measure_time
    def save(self,filename):
        with FileManage(filename) as f:
            for line in self.generate_date():
                f.write(line+"\n")
        print("REPORT SAVED SUCCESSFULLY.")

class TextReport(Report):
    def generate_date(self):
        for num in range(5):
            yield f"Text Report Line{num+1}"

class StructuredReport(Report):
    def generate_date(self):
        for num in range(5):
            yield f"Text Report Line{num+1}, value: line_detail{num+1}"

if __name__=="__main__":
    print("Type 1 for a standard text report")
    print("Type 2 for a detailed report")

    choice=int(input("Enter choice: "))

    if choice == 1:
        report = TextReport()
        filename="text_report.txt"
    elif choice == 2:
        report = StructuredReport()
        filename="structured_report.txt"
    else:
        print("Invalid choice")
        exit()

    report.save(filename)
