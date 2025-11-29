export default async function buscarDados() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve([10, 20, 30, 40]);
        }, 500);
    });
}