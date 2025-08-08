#include <stdio.h>

void movimento_torre(int num){
    if (num >= 0 && num < 5){
        movimento_torre(num + 1);
        printf("Direita\n");
    }
};

void movimento_bispo(int num){
    if (num > 0){
        printf("Cima e Direita\n");
        movimento_bispo(num - 1);
    }
};

void movimento_rainha(int num){
    if (num > 0 && num <= 8){
        printf("Cima e Direita - %d\n", num);
        movimento_rainha(num+1);
    }
};

int main() {
    
    int count_torre = 0, count_bispo = 0, count_rainha = 1, count_cavalo_horizontal = 1, count_cavalo_vertical;

    // Torre 
    printf("\nTORRE\n");
    movimento_torre(0);
    
    // Bispo 
    printf("\nBISPO\n");
    movimento_bispo(5);
    
    // Rainha
    printf("\nRAINHA\n");
    movimento_rainha(1);
    
    // Cavalo
    printf("\nCAVALO\n");
    for (count_cavalo_horizontal; count_cavalo_horizontal <=2; count_cavalo_horizontal++){
        
        count_cavalo_vertical = 1;
        
        printf("Baixo\nBaixo\n");
        while (count_cavalo_vertical <=1)
        {
            printf(" Esquerda\n");
            count_cavalo_vertical++;
            if (count_cavalo_vertical > 2) break;
        };


    }

    return 0;

}