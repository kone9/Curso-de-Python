pi=3.141516
l1 = ["Numero","Letra",[23, pi,278],"variable"]
print l1.index("variable")

pi=3.141516
l1 = ["Numero","Letra",[23, pi,278],"variable"]
print l1.append("constante")

pi=3.141516
l1 = ["Numero","Letra",[23, pi,278],"variable"]
print l1.count("variable")

pi=3.141516
l1 = ["Numero","Letra",[23, pi,278],"variable"]
print l1.insert(2,"valor nuevo")

pi=3.141516
l1 = ["Numero","Letra",[23, pi,278],"variable"]
l2=["Cesar","Mario","Octavio"]
l1.extend(l2)
print l1

l1 = ["Numero","Letra",[23, pi,278],"variable"]
l1.pop(2)
print l1

l1 = ["Numero","Letra","Numero","variable"]
l1.remove("Numero")
print l1

l1 = ["Numero","Letra",[23, pi ,278],"variable"]
l1.reverse()
print l1