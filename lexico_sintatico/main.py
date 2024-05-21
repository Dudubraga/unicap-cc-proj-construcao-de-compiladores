from lexer import lexer
from parser import parser

code = """
int main() {
    int numero1 = 123;
    int numero2 = 456;
    int resultado = numero1 + numero2;
    return resultado;
}
float calcularMedia(float nota1, float nota2) {
    float media = (nota1 + nota2) / 2.0;
    if (media >= 6.0) {
        printf("Aprovado!");
    } else {
        printf("Reprovado.");
    }
    return media;
}
void saudacao() {
    char mensagem[] = "Olá, mundo!";
    int numero = 42;
    printf(mensagem);
    printf("O número é: " + numero);
}
// Este é um comentário de linha.
int dobrar(int x) {
    /* Este é um comentário
    de múltiplas linhas. */
    return x * 2;
}
void imprimirValores(int valores[]) {
    for (int i = 0; i < valores.length; i++) {
        printf("Valor[" + i + "] = " + valores[i]);
    }
}
"""

lexer.input(code)
for token in lexer:
    print(token)

result = parser.parse(code)
print(result)