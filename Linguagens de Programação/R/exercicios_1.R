'''
1. Classificação do Combustível do Meio de Transporte: Crie uma função chamada
classifica_combustivel que recebe o nome de um meio de transporte como argumento e
retorna o tipo de combustível que esse meio de transporte utiliza. Considere os seguintes meios
de transporte e seus respectivos tipos de combustível:

Carro: Gasolina, Diesel, Eletrecidade ou Gás Natural
Moto: Gasolina
Bicicleta: Humana (sem combustível)
Ônibus: Diesel ou Gás Natural
Trem: Eletricidade ou Diesel
Avião: Querosene
Barco: Diesel ou Gasolina
'''

classifica_combustivel <- function()  {
  
  meio_transporte <- readline("Digite o nome do meio de transporte: ")
  
  if(meio_transporte == "Carro") {
    combustivel <- "Gasolina, Diesel, Eletrecidade ou Gás Natural"
  } else if(meio_transporte == "Moto") {
    combustivel <- "Gasolina"
  } else if(meio_transporte == "Bicicleta") {
    combustivel <- "Humana (sem combustível)"
  } else if(meio_transporte == "Ônibus") {
    combustivel <- "Diesel ou Gás Natural"
  } else if(meio_transporte == "Trem") {
    combustivel <- "Eletricidade ou Diesel"
  } else if(meio_transporte == "Avião") {
    combustivel <- "Querosene"
  } else if(meio_transporte == "Barco") {
    combustivel <- "Diesel ou Gasolina"
  }
  
  cat("O combustível utilizado em", meio_transporte, "é", combustivel)
  
}

classifica_combustivel()

'''
2. Conversão de Temperatura: Crie uma função chamada converte_temperatura que recebe uma
temperatura em graus Celsius ou Fahrenheit como argumento e converte para graus Celsius ou
Fahrenheit. A função recebe dois argumentos: A temperatura e a unidade de medida
correspondente.
'''

converte_temperatura <- function(temperatura,unidade) {
  
  if(unidade == "Celsius"){
    valor_convertido <- temperatura * 1.8 + 32
  } else if (unidade == "Fahrenheit"){
    valor_convertido <- (temperatura - 32)/1.8 
  }
  
  cat("A temperatura convertida é", valor_convertido, "graus")
}

converte_temperatura(30,"Celsius")

'''
3. Calculadora de IMC: Crie uma função chamada calcula_imc que recebe o peso (em quilogramas) e a altura (em metros) de uma pessoa como argumentos e calcula o Índice de Massa
Corporal (IMC). A função deve retornar o IMC calculado e uma mensagem que classifica a pessoa
em uma das seguintes categorias: “Abaixo do Peso”, “Peso Normal”, “Sobrepeso” ou “Obesidade”.
'''

calcula_imc <- function(peso,altura) {
  
  imc <- peso / altura^2
  
  if(imc <= 18.5) {
    resultado <- "Abaixo do peso"
  } else if(imc >= 18.6 & imc <= 24.9){
    resultado <- "Peso Normal"
  } else if(imc >= 25 & imc <= 29.9){
    resultado <- "Sobrepeso"
  } else if(imc >= 30){
    resultado <- "Obesidade"
  } 
    
  cat("O seu IMC é", imc, "e a sua classificação é", resultado) 
}

calcula_imc(70,1.75)
