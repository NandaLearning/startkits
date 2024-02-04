import subprocess

def create_react_project(project_name):
    command = f"npm create vite@latest {project_name} -- --template react"
    subprocess.run(command, shell=True)

def create_laravel_project(project_name):
    command = f"composer create-project --prefer-dist laravel/laravel {project_name}"
    subprocess.run(command, shell=True)


def main():
    print("\n")
    print("  AAAAA  TTTTTT  EEEEE  N   N  GGG  ")
    print(" A     A   T     E      NN  N G   G ")
    print(" AAAAAAA   T     EEEEE  N N N G     ")
    print(" A     A   T     E      N  NN G   GG")
    print(" A     A   T     EEEEE  N   N  GGGG ")
    print("\n")  # Tambahkan spasi pada awal baris ini


    print("Selamat datang di StartKits by NandaLearning !")
    print("\n")
    print("Pilih framework yang ingin Anda gunakan:")
    print("1. React JS")
    print("2. Laravel")

    choice = input("Masukkan nomor pilihan framework: ")

    if choice == "1":
        project_name = input("Masukkan nama proyek React JS: ")
        create_react_project(project_name)
        print(f"Proyek React JS '{project_name}' berhasil dibuat!")

    elif choice == "2":
        project_name = input("Masukkan nama proyek Laravel: ")
        create_laravel_project(project_name)
        print(f"Proyek Laravel '{project_name}' berhasil dibuat!")

    else:
        print("Pilihan tidak valid. Silakan pilih nomor yang benar.")

if __name__ == "__main__":
    main()
