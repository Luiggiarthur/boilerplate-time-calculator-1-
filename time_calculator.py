def add_time(start, duration, seman=""):
    Listasemana = seman
    horas = start.split()
    day = 0
    hora = (horas[0].split(':'))
    h = int(hora[0])
    minuto = int(hora[1])
    periodo = horas[1]


    if seman:
      semana = ["Sunday" , "Monday" , "tuesday" , "Wednesday" , "Thursday" , "Friday" , "saturDay"]
      seman = semana.index(Listasemana)
    
    
    durac = duration.split(':')
    d_hour = int(durac[0])
    d_min =int(durac[1])
    
    new_min = minuto+d_min
    
    #calculo minutos a mais
    if new_min > 59:
    
            new_min = new_min - 60
            d_hour = d_hour + 1
    
    
    #calculo dias a mais
    
       
    d_mais = d_hour/24
    if d_mais >= 1:
    
            day = int(d_mais)
            #d_hour = d_hour + (d_hour % 24)
            
            new_hour = h + (d_hour - 24*day)
    else:
            new_hour = h + d_hour
    
    
    if "PM" in start and new_hour >= 12:
        if new_hour == 12:
            day = day + 1
            new_hour = new_hour
            periodo = "AM"
        else:    
            day = day + 1
            new_hour = new_hour - 12
            periodo = "AM"
    elif "AM" in start and new_hour >= 12:
         if new_hour == 12:
            new_hour = new_hour
            periodo = "PM" 
         else:   
            new_hour = new_hour - 12
            periodo = "PM"      
    if seman:  
      if seman + day < 7:
            dia_semana = seman + day
            DiadaSemana = semana[dia_semana]
      else:
            num_semanas = int((seman+day)/7)
            diaS = (seman + day )
            dia_semana = (diaS - 7*(num_semanas) )
            DiadaSemana = semana[dia_semana]
    else:
            seman =""
            
    
    if new_min < 10:        
            new_min = str("0") + str(new_min)
    
    if seman:  
      if day < 1:
              new_time = str(new_hour) + ":" + str(new_min) +" "+  periodo + ", " + str(DiadaSemana)
      elif day == 1:
              new_time = (str(new_hour) + ":" + str(new_min) + " "+ str(periodo) + ", " + DiadaSemana +" "+ "(next day)")
              
      else:
              new_time = str(new_hour) + ":" + str(new_min) +" "+  str(periodo) + ", " + DiadaSemana +" "+ "(" + str(day) + " days later)"
    else:
  
      if day < 1:
              new_time = str(new_hour) + ":" + str(new_min) +" "+  periodo 
      elif day == 1:
              new_time = (str(new_hour) + ":" + str(new_min) +" "+  str(periodo) +" "+ "(next day)")
              
      else:
              new_time = str(new_hour) + ":" + str(new_min) + " "+ str(periodo) +" "+  "(" + str(day) + " days later)"

    return new_time
