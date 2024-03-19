class Node:
    def __init__(self, id_gereja, nama, alamat, tahun_berdiri):
        self.id_gereja = id_gereja
        self.nama = nama
        self.alamat = alamat
        self.tahun_berdiri = tahun_berdiri
        self.next = None

class GerejaLinkedList:
    def __init__(self):
        self.head = None

    def create_data(self, id_gereja, nama, alamat, tahun_berdiri):
        new_node = Node(id_gereja, nama, alamat, tahun_berdiri)
        new_node.next = self.head
        self.head = new_node
        print(f'Data gereja dengan ID {id_gereja} berhasil ditambahkan.')

    def read_data(self, id_gereja=None):
        current = self.head

        if id_gereja:
            while current:
                if current.id_gereja == id_gereja:
                    print(f'Data gereja dengan ID {id_gereja}:')
                    print(f'ID Gereja: {current.id_gereja}')
                    print(f'Nama: {current.nama}')
                    print(f'Alamat: {current.alamat}')
                    print(f'Tahun Berdiri: {current.tahun_berdiri}')
                    return
                current = current.next
            print(f'Data gereja dengan ID {id_gereja} tidak ditemukan.')
        else:
            print('Data seluruh gereja:')
            while current:
                print(f'ID Gereja: {current.id_gereja}')
                print(f'Nama: {current.nama}')
                print(f'Alamat: {current.alamat}')
                print(f'Tahun Berdiri: {current.tahun_berdiri}')
                print()
                current = current.next

    def update_data(self, id_gereja, field, value):
        current = self.head

        while current:
            if current.id_gereja == id_gereja:
                if hasattr(current, field):
                    setattr(current, field, value)
                    print(f'Data {field} gereja dengan ID {id_gereja} berhasil diperbarui.')
                    return
                else:
                    print(f'Field {field} tidak valid.')
                    return
            current = current.next

        print(f'Data gereja dengan ID {id_gereja} tidak ditemukan.')

    def delete_data(self):
        if self.head:
            deleted_node = self.head
            self.head = self.head.next
            print(f'Data gereja dengan ID {deleted_node.id_gereja} berhasil dihapus.')
        else:
            print('Tidak ada data gereja untuk dihapus.')

    def quick_sort(self):
        self.head = self._quick_sort(self.head)

    def _quick_sort(self, start):
        if start is None or start.next is None:
            return start

        pivot = start.id_gereja
        lesser_head = None
        equal_head = None
        greater_head = None
        current = start

        while current:
            if current.id_gereja < pivot:
                if lesser_head is None:
                    lesser_head = Node(current.id_gereja, current.nama, current.alamat, current.tahun_berdiri)
                else:
                    lesser_head.next = Node(current.id_gereja, current.nama, current.alamat, current.tahun_berdiri)
            elif current.id_gereja == pivot:
                if equal_head is None:
                    equal_head = Node(current.id_gereja, current.nama, current.alamat, current.tahun_berdiri)
                else:
                    equal_head.next = Node(current.id_gereja, current.nama, current.alamat, current.tahun_berdiri)
            else:
                if greater_head is None:
                    greater_head = Node(current.id_gereja, current.nama, current.alamat, current.tahun_berdiri)
                else:
                    greater_head.next = Node(current.id_gereja, current.nama, current.alamat, current.tahun_berdiri)

            current = current.next

        sorted_head = self._quick_sort(lesser_head)
        if equal_head:
            if sorted_head:
                current = sorted_head
                while current.next:
                    current = current.next
                current.next = equal_head
            else:
                sorted_head = equal_head

        greater_sorted = self._quick_sort(greater_head)
        if sorted_head:
            current = sorted_head
            while current.next:
                current = current.next
            current.next = greater_sorted
        else:
            sorted_head = greater_sorted

        return sorted_head



    def fibonacci_search(self):
        ids = []
        current = self.head
        while current:
            ids.append(current.id_gereja)
            current = current.next

        def fibonacci_search_helper(arr, x):
            fib_m_minus_2 = 0
            fib_m_minus_1 = 1
            fib_m = fib_m_minus_1 + fib_m_minus_2

            while fib_m < len(arr):
                fib_m_minus_2, fib_m_minus_1 = fib_m_minus_1, fib_m
                fib_m = fib_m_minus_1 + fib_m_minus_2

            offset = -1

            while fib_m > 1:
                i = min(offset + fib_m_minus_2, len(arr) - 1)
                if arr[i] == x:
                    return i
                elif arr[i] < x:
                    fib_m, fib_m_minus_1 = fib_m_minus_1, fib_m_minus_2
                    fib_m_minus_2 = fib_m - fib_m_minus_1
                    offset = i
                else:
                    fib_m, fib_m_minus_1 = fib_m_minus_2, fib_m_minus_1
                    fib_m_minus_2 = fib_m - fib_m_minus_1

            if fib_m_minus_1 and offset < len(arr) - 1 and arr[offset + 1] == x:
                return offset + 1
            
            return -1

        ids.sort(key=lambda x: fibonacci_search_helper(ids, x))

        new_head = None
        for id_gereja in ids:
            current = self.head
            while current:
                if current.id_gereja == id_gereja:
                    if new_head is None:
                        new_head = Node(id_gereja, current.nama, current.alamat, current.tahun_berdiri)
                    else:
                        temp = new_head
                        while temp.next:
                            temp = temp.next
                        temp.next = Node(id_gereja, current.nama, current.alamat, current.tahun_berdiri)
                    break
                current = current.next

        self.head = new_head


def main():
    gereja_list = GerejaLinkedList()

    while True:
        print("\nMenu:")
        print("1. Tambah Data Gereja")
        print("2. Tampilkan Data Gereja")
        print("3. Perbarui Data Gereja")
        print("4. Hapus Data Gereja")
        print("5. Urutkan Data Gereja")
        print("6. Keluar")

        pilihan = input("Silakan masukkan pilihan anda: ")

        if pilihan == '1':
            id_gereja = input("Masukkan ID gereja: ")
            nama = input("Masukkan nama gereja: ")
            alamat = input("Masukkan alamat lengkap gereja: ")
            tahun_berdiri = input("Masukkan tahun berdiri gereja tersebut: ")
            gereja_list.create_data(id_gereja, nama, alamat, tahun_berdiri)

        elif pilihan == '2':
            id_gereja = input("Masukkan ID Gereja untuk menampilkan data Gereja: ")
            gereja_list.read_data(id_gereja)

        elif pilihan == '3':
            id_gereja = input("Masukkan ID Gereja: ")
            field = input("Masukkan Nama Field yang Ingin Diperbarui: ")
            value = input("Masukkan Nilai Baru: ")
            gereja_list.update_data(id_gereja, field, value)

        elif pilihan == '4':
            gereja_list.delete_data()

        elif pilihan == '5':
            gereja_list.fibonacci_search()
            print("Data gereja berhasil diurutkan secara berdasarkan ID.")

        elif pilihan == '6':
            print("Terima kasih! Program selesai.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan pilih ulang")


if __name__ == "__main__":
    main()































def fibonacci_search(self, id_gereja):

    fib_m_minus_2 = 0
    fib_m_minus_1 = 1
    fib_m = fib_m_minus_1 + fib_m_minus_2

    
    while fib_m < self.length():
        fib_m_minus_2 = fib_m_minus_1
        fib_m_minus_1 = fib_m
        fib_m = fib_m_minus_1 + fib_m_minus_2

    offset = -1  

    while fib_m > 1:
        i = min(offset + fib_m_minus_2, self.length() - 1)

        
        if self.get_id_at_index(i) == id_gereja:
            return i

        
        elif self.get_id_at_index(i) < id_gereja:
            fib_m = fib_m_minus_1
            fib_m_minus_1 = fib_m_minus_2
            fib_m_minus_2 = fib_m - fib_m_minus_1
            offset = i

        
        else:
            fib_m = fib_m_minus_2
            fib_m_minus_1 = fib_m_minus_1 - fib_m_minus_2
            fib_m_minus_2 = fib_m - fib_m_minus_1

    
    if fib_m_minus_1 and offset < self.length() - 1 and self.get_id_at_index(offset + 1) == id_gereja:
        return offset + 1

    
    return -1

def get_id_at_index(self, index):
    current = self.head
    for _ in range(index):
        current = current.next
    return current.id_gereja

def length(self):
    count = 0
    current = self.head
    while current:
        count += 1
        current = current.next
    return count

def quick_sort(self):
    id_gereja = input("Masukkan ID Gereja untuk pencarian (Fibonacci Search): ")

    result = self.fibonacci_search(id_gereja)

    if result != -1:
        print(f"Data gereja dengan ID {id_gereja} ditemukan pada indeks {result}.")
    else:
        print(f"Data gereja dengan ID {id_gereja} tidak ditemukan.")


