// Desafio Super Trunfo - Países
#include <stdio.h>
int main() {
    // Sugestão: Defina variáveis separadas para cada atributo da cidade.
    char estado, estado2;
    char nome_cidade[15], nome_cidade2[15], codigo_carta[3], codigo_carta2[3];
    int populacao, populacao2, pontos_turisticos, pontos_turisticos2;
    float area, area2, pib,pib2;

    printf("Digite abaixo as informações solicitadas para compor sua PRIMEIRA carta.\n");
    
    // Cadastro das Cartas: 
    printf("Digite o Estado\n");
    scanf(" %c", &estado); // o espaçõ antes do especificador de formato garante que o coódigo funcione de maneira adequada, pois quando não há espaço a linguaguem ainda permanece no mesmo espaço de entrada

    printf("Digite o Código da Carta\n");
    scanf("%s", &codigo_carta[0]);
    
    printf("Digite o Nome da Cidade\n");
    scanf("%s", &nome_cidade[0]);
 
    printf("Digite a População\n");
    scanf("%d", &populacao);

    printf("Digite a Área (em km²)\n");
    scanf("%f", &area);
 
    printf("Digite o PIB\n");
    scanf("%f", &pib);

    printf("Digite o Número de Pontos Turísticos\n");
    scanf("%d", &pontos_turisticos);
    
    //calcula os dados da cidade
    densidade_populacional = populacao / area;
    pib_per_capita = pib / populacao;
        
    // Exibição dos Dados das Cartas:
    printf("Carta 1:\n Estado: %c\n Código: %s\n Nome da Cidade: %s\n População: %d\n Área: %.3fkm²\n PIB: R$ %.2f\n Número de Pontos Turísticos: %i\n", estado, codigo_carta, nome_cidade, populacao, area, pib, pontos_turisticos);
    printf("Densidade Populacional: %.2f\n", densidade_populacional);
    printf("PIB per Capita: %.2f\n", pib_per_capita);
    
    printf("\n \n");

    // Cadastro das Cartas:
    printf("Digite abaixo as informações solicitadas para compor sua SEGUNDA carta.\n");
    
    printf("Digite o Estado\n");
    scanf(" %c", &estado2);

    printf("Digite o Código da Carta\n");
    scanf("%s", &codigo_carta2[0]);
    
    printf("Digite o Nome da Cidade\n");
    scanf("%s", &nome_cidade2[0]);
 
    printf("Digite a População\n");
    scanf("%d", &populacao2);

    printf("Digite a Área (em km²)\n");
    scanf("%f", &area2);
 
    printf("Digite o PIB\n");
    scanf("%f", &pib2);

    printf("Digite o Número de Pontos Turísticos\n");
    scanf("%d", &pontos_turisticos2);

    //calcula os dados da cidade
    densidade_populacional2 = populacao2 / area2;
    pib_per_capita2 = pib2 / populacao2;
    
    // Exibição dos Dados das Cartas:
    printf("Carta 2:\n Estado: %c\n Código: %s\n Nome da Cidade: %s\n População: %d\n Área: %.3fkm²\n PIB: R$ %.2f\n Número de Pontos Turísticos: %i\n", estado2, codigo_carta2, nome_cidade2, populacao2, area2, pib2, pontos_turisticos2);
    printf("Densidade Populacional: %.2f\n", densidade_populacional2);
    printf("PIB per Capita: %.2f\n", pib_per_capita2);
    return 0;
}