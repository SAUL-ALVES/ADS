export function calcularMedia(array) {
    if (!Array.isArray(array) || array.length === 0) return 0;
    return array.reduce((acc, n) => acc + n, 0) / array.length;
}

export const VALOR_PI = 3.14;