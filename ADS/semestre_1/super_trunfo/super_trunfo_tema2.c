#include <stdio.h>
#include <string.h>

int main()
{

    char estado, estado2;
    char nome_cidade[15], nome_cidade2[15], codigo_carta[3], codigo_carta2[3];
    unsigned long int populacao, populacao2;
    int pontos_turisticos, pontos_turisticos2, resultado;
    float area, area2, pib, pib2, densidade_populacional, densidade_populacional2, pib_per_capita, pib_per_capita2, super_poder, super_poder2;

    // solicita informações para primeira carta
    printf("**Digite abaixo as informações solicitadas para compor sua PRIMEIRA carta.**\n");

    printf("Digite o Estado\n");
    scanf(" %c", &estado);

    printf("Digite o Código da Carta\n");
    scanf("%s", codigo_carta);

    printf("Digite o Nome do País\n");
    scanf("%s", nome_cidade);

    printf("Digite a População\n");
    scanf("%ld", &populacao);

    printf("Digite a Área (em km²)\n");
    scanf("%f", &area);

    printf("Digite o PIB\n");
    scanf("%f", &pib);

    printf("Digite o Número de Pontos Turísticos\n");
    scanf("%d", &pontos_turisticos);

    // solicita informações para a segunda carta
    printf("**Digite abaixo as informações solicitadas para compor sua SEGUNDA carta.**\n");

    printf("Digite o Estado\n");
    scanf(" %c", &estado2);

    printf("Digite o Código da Carta\n");
    scanf("%s", codigo_carta2);

    printf("Digite o Nome do País\n");
    scanf("%s", nome_cidade2);

    printf("Digite a População\n");
    scanf("%ld", &populacao2);

    printf("Digite a Área (em km²)\n");
    scanf("%f", &area2);

    printf("Digite o PIB\n");
    scanf("%f", &pib2);

    printf("Digite o Número de Pontos Turísticos\n");
    scanf("%d", &pontos_turisticos2);

    // calculo da densidade populacional
    densidade_populacional = populacao / area;
    densidade_populacional2 = populacao2 / area2;

    // calculo do pib per capita
    pib_per_capita = pib / populacao;
    pib_per_capita2 = pib2 / populacao2;

    // calculo do super poder
    super_poder = area + pib + pontos_turisticos;
    super_poder2 = area2 + pib2 + pontos_turisticos2;

    // imprime na tela informações das cartas
    printf("Carta 1:\n Estado: %c\n Código: %s\n Nome do País: %s\n População: %ld\n Área: %.3fkm²\n PIB: R$ %.2f\n Número de Pontos Turísticos: %i\n\n", estado, codigo_carta, nome_cidade, populacao, area, pib, pontos_turisticos);
    printf("Densidade Populacional: %.2f\n", densidade_populacional);
    printf("PIB Per Capita: %.2f\n", pib_per_capita);
    printf("SUPER_PODER: %2.f\n", super_poder);

    printf("Carta 2:\n Estado: %c\n Código: %s\n Nome do País: %s\n População: %ld\n Área: %.3fkm²\n PIB: R$ %.2f\n Número de Pontos Turísticos: %i\n\n", estado2, codigo_carta2, nome_cidade2, populacao2, area2, pib2, pontos_turisticos2);
    printf("Densidade Populacional: %.2f\n", densidade_populacional2);
    printf("PIB per Capita: %.2f\n", pib_per_capita2);
    printf("SUPER_PODER: %.2f\n", super_poder2);

    if (super_poder > super_poder2)
    {
        printf("CARTA VENCEDORA: %s, cidade de %s\n", codigo_carta, nome_cidade);
    }
    else
    {
        printf("CARTA VENCEDORA: %s, cidade de %s\n", codigo_carta2, nome_cidade2);
    }

    printf("SUPER_PODER CARTA 1: %.2f\n SUPER_PODER CARTA 2: %.2f\n", super_poder, super_poder2);

    // menu interativo
    int atributo;
    char att2;

    printf("Escolha o atributo que deseja comparar \n");
    printf(" 1 - Nome do país\n 2 - População\n 3 - Área\n 4 - PIB\n 5 - Número de pontos turísticos\n 6 - Densidade demográfica\n");
    scanf(" %d", &atributo);

    // comparação de um atributo
    switch (atributo)
    {
    case 1:
        printf("Você escolheu Nome da Cidade\n");
        printf("Carta 1: %s \n", nome_cidade);
        printf("Carta 2: %s \n", nome_cidade2);
        printf("Nessa escolha não há cidade vencedora.\n");
        break;
    case 2:
        printf("Você escolheu População\n");
        printf("Carta 1: %s | %ld \n", nome_cidade, populacao);
        printf("Carta 2: %s | %ld \n", nome_cidade2, populacao2);

        if (populacao > populacao2){
            printf("A cidade *** %s *** venceu!!!\n", nome_cidade);
        }
        else{
            printf("A cidade *** %s *** venceu!!!\n", nome_cidade2);
        }        
        break;
    case 3:
        printf("Você escolheu Área\n");
        printf("Carta 1: %s | %f \n", nome_cidade, area);
        printf("Carta 2: %s | %f \n", nome_cidade2, area2);

        if (area > area2){
            printf("A cidade *** %s *** venceu!!!\n", nome_cidade);
        }
        else{
            printf("A cidade *** %s *** venceu!!!\n", nome_cidade2);
        }
        break;

    case 4:
        printf("Você escolheu PIB\n");
        printf("Carta 1: %s | %f \n", nome_cidade, pib);
        printf("Carta 2: %s | %f \n", nome_cidade2, pib2);

        if (pib > pib2){
            printf("A cidade *** %s *** venceu!!!\n", nome_cidade);
        }
        else{
            printf("A cidade *** %s *** venceu!!!\n", nome_cidade2);
        }
        break;

    case 5:
        printf("Você escolheu Pontos Turísticos \n");
        printf("Carta 1: %s | %d \n", nome_cidade, pontos_turisticos);
        printf("Carta 2: %s | %d \n", nome_cidade2, pontos_turisticos2);

        if (pontos_turisticos > pontos_turisticos2){
            printf("A cidade *** %s *** venceu!!!\n", nome_cidade);
        }
        else{
            printf("A cidade *** %s *** venceu!!!\n", nome_cidade2);
        }
        break;

    case 6:
        printf("Você escolheu Densidade Populacional\n");
        printf("Carta 1: %s | %f \n", nome_cidade, densidade_populacional);
        printf("Carta 2: %s | %f \n", nome_cidade2, densidade_populacional2);

        if (densidade_populacional2 < densidade_populacional){
            printf("A cidade *** %s *** venceu!!!\n", nome_cidade2);
        }
        else{
            printf("A cidade *** %s *** venceu!!!\n", nome_cidade);
        }
        break;

    default:
        printf("Por favor, escolha um número entre 1 e 6. \n");
        break;
    }

    return 0;
}
// https://github.com/Cursos-TI/desafio-cadastro-das-cartas-no-super-trunfo-geicecs50