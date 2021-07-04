import csv
from datetime import datetime
from math import sqrt, pi, cos, log10
from typing import List

class Solution:

    def __init__(self, fileName):
        # id,first_name,last_name,dateOfBirth,interests,latitude,longitude
        self.students = []
        with open(fileName) as file:
            reader = csv.reader(file, delimiter=',', skipinitialspace=True)
            i = 0
            for line in reader:
                self.students.append(line[1:])
                # Se convierten los tipos de datos correspondientes
                self.students[i][2] = datetime.strptime(self.students[i][2], '%Y-%m-%d')
                self.students[i][3] = float(self.students[i][3])
                self.students[i][4] = float(self.students[i][4])
                for j in range(5, 11):
                    self.students[i][j] = bool(int(self.students[i][j]))

                i += 1



    # Distancia entre estudiantes
    def ejercicio1(self, id1, id2):

        def radians(n):
            degrees = n

            radians = degrees * (pi / 180)
            return radians

        lat1 = self.students[id1-1][3]
        long1 = self.students[id1-1][4]
        lat2 = self.students[id2-1][3]
        long2 = self.students[id2-1][4]
        # lat1 = -12.018166
        # long1 = -77.107543
        # lat2 = -12.135093
        # long2 = -77.022227
        dlat = lat1 - lat2
        dlong = long1 - long2

        EARTH = 6371.009
        
        a = radians(dlat)**2
        c = (radians(lat1) + radians(lat2))/2
        b = radians(dlong) * cos(c)

        d = EARTH * sqrt(a + (b**2))
        
        return d


    # Compatibilidad entre estudiantes
    def ejercicio2(self, id1, id2):
        d = self.ejercicio1(id1, id2)
        
        stu1 = self.students[id1-1]
        stu2 = self.students[id2-1] 

        birth1 = stu1[2]
        birth2 = stu2[2]

        agedelta = abs(birth1 - birth2).days / 365

        if agedelta <= 1:
            e = 1
        else:
            e = (agedelta)**(-1)

        coin = 0

        for x in range(5,11):
            if self.students[id1-1][x] == self.students[id2-1][x]:
                coin += 1
        
        compatibilidad = (log10(d))**-1 + e + coin

        return compatibilidad

    # Estudiantes mas cercanos
    def ejercicio3(self, id, n):
        distances = []
        relation = {}
        for i in range(1,self.students.__len__()):
            if i == id: continue
            dis = self.ejercicio1(id,i)
            distances.append(dis)
            relation[dis] = i

        distances.sort()
        stu = []
        for i in distances[:n]:
            stu.append(relation[i])
               
        return stu
            
            


    # Estudiantes mas cercanos
    def ejercicio4(self, id, n):
        distances = []
        relation = {}
        for i in range(1,self.students.__len__()):
            if i == id: continue
            dis = self.ejercicio1(id,i)
            distances.append(dis)
            relation[dis] = i


        distances.sort(reverse=True)
        stu = []
        for i in distances[:n]:
            stu.append(relation[i])
               
        return stu

    def ejercicio5(self, id, n):
        compatibles = []
        relation = {}
        for i in range(1,self.students.__len__()):
            if i == id: continue
            comp = self.ejercicio2(id,i)
            compatibles.append(comp)
            relation[comp] = i


        compatibles.sort(reverse=True)
        stu = []
        for i in compatibles[:n]:
            stu.append(relation[i])
               
        return stu

    def ejercicio6(self, id, n):
        compatibles = []
        relation = {}
        for i in range(1,self.students.__len__()):
            if i == id: continue
            comp = self.ejercicio2(id,i)
            compatibles.append(comp)
            relation[comp] = i


        compatibles.sort()
        stu = []
        for i in compatibles[:n]:
            stu.append(relation[i])
               
        return stu
s = Solution("/Users/italoamaya/PycharmProjects/SandBox/Tareas/Tarea2/data.csv")
print(s.ejercicio1(9,27))
print(s.ejercicio2(5,10))
print(s.ejercicio3(5,10))
print(s.ejercicio4(5,10))
print(s.ejercicio5(5,10))
print(s.ejercicio6(5,10))
