def search_patients_by_disease(patients, disease):
    result = [patient["Name"] for patient in patients if patient["Disease"].lower() == disease.lower()]
    return result
patients = []
num_patients = int(input("Enter the number of patients:"))
for _ in range(num_patients):
    name = input("Enter patient's name:")
    age = int(input(f"Enter {name}'s age:"))
    disease = input(f"Enter {name}'s disease:")
    patients.append({"Name": name, "Age": age, "Disease": disease})
search_disease = input("Enter the disease to search for:")
patients_with_disease = search_patients_by_disease(patients, search_disease)
if patients_with_disease:
    print(f"Patients with {search_disease}: {patients_with_disease}")
else:
    print(f"No patients found with disease '{search_disease}'")
