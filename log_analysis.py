from collections import Counter

def analisar_logs(arquivo):
    with open(arquivo, "r") as f:
        linhas = f.readlines()

    ips = []
    falhas = 0

    for linha in linhas:
        partes = linha.split(" - ")
        ip = partes[0]
        status = partes[1].strip()

        ips.append(ip)

        if "falha" in status:
            falhas += 1

    contagem_ips = Counter(ips)

    print("\n🔎 Análise de Logs\n")
    print(f"Total de tentativas com falha: {falhas}\n")

    print("IPs mais frequentes:")
    for ip, count in contagem_ips.items():
        print(f"{ip}: {count} acessos")

    print("\n⚠️ Possíveis IPs suspeitos:")
    for ip, count in contagem_ips.items():
        if count > 2:
            print(f"{ip} (muitas tentativas)")


if __name__ == "__main__":
    analisar_logs("log.txt")
