#include <stdio.h>
int main(){

    // #define LINHAS 3
    // #define COLUNAS 3

    // int matriz[LINHAS][COLUNAS];
    // int soma = 1;

    // for(int a = 0; a < LINHAS; a++){
    //     for(int b = 0; b < COLUNAS; b++){
    //         matriz[a][b] = soma;
    //         soma++;
    //         printf("%d", matriz[a][b]);
    //     }
    //     printf("\n");
    // }

    int tabuleiro[10][10] = {
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
    };

    int navio1_linha = 3, navio1_coluna = 4;
    int navio2_linha = 1, navio2_coluna = 7;

    for (int i = 0; i < 10; i++){
        for (int j = 0; j < 10; j++){
            if (tabuleiro[i] == tabuleiro[navio1_linha] 
                && tabuleiro[j] == tabuleiro[navio1_coluna]){
                    tabuleiro[i][j] = 3;
                    if (j > 0 && j < 10){
                        tabuleiro[i][j - 1] = 3; // faz caminhar a coluna, na horizontal
                        tabuleiro[i][j + 1] = 3;
                    }
            }
            
        };
    };

    int octaedro_coluna = 2, octaedro_linha = 1, cone = 5, cruz_coluna = 3, cruz_linha = 8;

    for (int i = 0; i < 10; i++){
        for (int j = 0; j < 10; j++){
            if (tabuleiro[i] == tabuleiro[octaedro_linha]
            && tabuleiro[j] == tabuleiro[octaedro_coluna]){
                tabuleiro[i][j] = 8;
                tabuleiro[i][j-1] = 8;
                tabuleiro[i][j+1] = 8;
                tabuleiro[i+1][j] = 8;
                tabuleiro[i-1][j] = 8;
            }
        };
    };

    for (int i = 0; i < 10; i++){
        for (int j = 0; j < 10; j++){
            if (tabuleiro[i] == tabuleiro[cruz_linha]
            && tabuleiro[j] == tabuleiro[cruz_coluna]){
                tabuleiro[i][j] = 1;
                tabuleiro[i][j-1] = 1;
                tabuleiro[i][j-2] = 1;
                tabuleiro[i][j+1] = 1;
                tabuleiro[i][j+2] = 1;
                tabuleiro[i+1][j] = 1;
                tabuleiro[i-1][j] = 1;
            }
        };
    };

    
    printf("\nTabuleiro:\n");
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            printf("%d ", tabuleiro[i][j]);
        }

        printf("\n"); 
    };
    return 0;
}