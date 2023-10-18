import os


PATH = fr"C:\Program Files\Java\jre-1.8\bin\java.exe"

# os.system(fr'cd C:\Git_Muzyria\Python\Python\My_Pixels_work\tcp_simulator_with_example')


os.system(fr'java -jar syncwise-tcp-simulator-0.6.jar --help')

os.system(fr'"{PATH}" -jar syncwise-tcp-simulator-0.6.jar -env live --request-type utilitygauge --device S10150000211018050 --limit 10')


