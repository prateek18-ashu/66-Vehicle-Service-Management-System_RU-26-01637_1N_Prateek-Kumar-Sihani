import os

class ServiceRecord:
    # Price list before GST
    PRICE_LIST = {
        "Oil Change": 1500,
        "Wheel Alignment": 800,
        "Full Service": 4500,
        "Brake Repair": 2200
    }

    def __init__(self, reg_no, owner, vehicle, service_type, status="Pending"):
        self.reg_no = reg_no
        self.owner = owner
        self.vehicle = vehicle
        self.service_type = service_type
        self.status = status

    def calculate_cost(self):
        """Calculates cost with 18% GST"""
        base_price = self.PRICE_LIST.get(self.service_type, 0)
        return base_price * 1.18

    def display(self):
        """Formats and returns record details"""
        cost = self.calculate_cost()
        return f"{self.reg_no} | {self.service_type} | Cost incl. 18% GST: Rs. {cost:.2f} | Status: {self.status}"


class VehicleServiceSystem:
    def __init__(self, filename="services.txt"):
        self.filename = filename
        self.records = {}
        self.load_from_file()

    def load_from_file(self):
        """Loads records from services.txt into dictionary"""
        if not os.path.exists(self.filename):
            return
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 5:
                        reg_no, owner, vehicle, service_type, status = parts
                        self.records[reg_no] = ServiceRecord(reg_no, owner, vehicle, service_type, status)
        except Exception as e:
            print(f"Error loading file: {e}")

    def save_to_file(self):
        """Saves all records from dictionary to services.txt"""
        try:
            with open(self.filename, "w") as f:
                for rec in self.records.values():
                    f.write(f"{rec.reg_no},{rec.owner},{rec.vehicle},{rec.service_type},{rec.status}\n")
        except Exception as e:
            print(f"Error saving file: {e}")

    def add_record(self, reg_no, owner, vehicle, service_type):
        """Add operation (C in CRUD)"""
        if service_type not in ServiceRecord.PRICE_LIST:
            print(f"Invalid service type. Choose from: {', '.join(ServiceRecord.PRICE_LIST.keys())}.")
            return False
        
        record = ServiceRecord(reg_no, owner, vehicle, service_type, "Pending")
        self.records[reg_no] = record
        self.save_to_file()
        print(f"Record added. {record.display()}")
        return True

    def view_records(self):
        """View operation (R in CRUD)"""
        if not self.records:
            print("No service records found.")
            return
        for rec in self.records.values():
            print(rec.display())

    def update_status(self, reg_no, new_status):
        """Update operation (U in CRUD)"""
        if reg_no in self.records:
            old_status = self.records[reg_no].status
            self.records[reg_no].status = new_status
            self.save_to_file()
            print(f"Status updated: {old_status} -> {new_status}")
            return True
        else:
            print(f"No record found for {reg_no}.")
            return False

    def delete_record(self, reg_no):
        """Delete operation (D in CRUD)"""
        if reg_no in self.records:
            del self.records[reg_no]
            self.save_to_file()
            print(f"Record for {reg_no} deleted.")
            return True
        else:
            print(f"No record found for {reg_no}.")
            return False


def main():
    system = VehicleServiceSystem()
    
    while True:
        print("\n--- Vehicle Service Management System ---")
        print("1. Add record")
        print("2. View records")
        print("3. Update status")
        print("4. Delete record")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ").strip()
        
        if choice == "1":
            reg_no = input("Reg no: ").strip()
            owner = input("Owner: ").strip()
            vehicle = input("Vehicle: ").strip()
            service_type = input("Service: ").strip()
            system.add_record(reg_no, owner, vehicle, service_type)
            
        elif choice == "2":
            system.view_records()
            
        elif choice == "3":
            reg_no = input("Reg no: ").strip()
            new_status = input("New status: ").strip()
            system.update_status(reg_no, new_status)
            
        elif choice == "4":
            reg_no = input("Reg no: ").strip()
            system.delete_record(reg_no)
            
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()