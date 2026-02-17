from abc import ABC, abstractmethod

class Report():
    def generate_report(self):
        self.parse()
        self.validate()
        self.save()

    @abstractmethod
    def parse(self):
        pass

    @abstractmethod
    def validate(self):
        pass
    
    @abstractmethod
    def save(self):
        pass

class StandardReport(Report):
    def parse(self):
        print("parsing the standard report...")
    def validate(self):
        print("validating the standard report...")
    def save(self):
        print("saving the standard report...")

class SpecialReport(Report):
    def generate_report(self):
        self.parse()
        self.validate()
        self.revalidate()
        self.save()

    def parse(self):
        print("parsing the special report...")

    def validate(self):
        print("validating the special report...")

    def revalidate(self):
        print("revalidating the special report...")

    def save(self):
        print("saving the special report...")

class PDF(StandardReport):
    def parse(self):
        print("working on the PDF report...")

class DOCX(StandardReport):
    def parse(self):
        print("working on the DOCX report...")

class TXT(StandardReport):
    def parse(self):
        print("working on the PDF report...")

class CSV(SpecialReport):
    def parse(self):
        print("working on the CSV report...")

class JSON(SpecialReport):
    def parse(self):
        print("working on the JSON report...")

class ReportFactory:
    @staticmethod
    def get_report(choice: int):
        if choice==1:
            return PDF()
        elif choice==2:
            return DOCX()
        elif choice==3:
            return TXT()
        elif choice==4:
            return CSV()
        elif choice==5:
            return JSON()
        else:
            raise ValueError("Invalid Input, Please try again..")

if __name__ == "__main__":
    
    try:
        choice = int(input(
            "Enter the type of report:\n"
            "Type 1 for PDF\n"
            "Type 2 for DOCX\n"
            "Type 3 for TXT\n"
            "Type 4 for CSV\n"
            "Type 5 for JSON\n"
        ))

        report=ReportFactory.get_report(choice)
        print("\nGenerating report...")
        report.generate_report()

    except ValueError as Value:
        print(f"Error: {Value}")

    except Exception as Excepting:
        print(f"Unexpected Error: {Excepting}")

    finally:
        print("Finished, exiting program...")