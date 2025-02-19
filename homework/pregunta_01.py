"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    import pandas as pd
    import matplotlib.pyplot as plt
    import os

    df = pd.read_csv("files/input/news.csv", index_col=0)
    plt.figure()

    colors = {"Television": "dimgray", "Internet": "tab:blue", 
              "Newspaper": "grey", "Radio": "lightgray"}
    
    zorder = {"Television": 4, "Internet": 3, "Newspaper": 2, "Radio": 1}

    linewidth = {"Television": 2, "Internet": 3, "Newspaper": 2, "Radio": 2}

    for column in df.columns:
        plt.plot(df[column], label=column, color=colors[column], zorder=zorder[column],
                linewidth=linewidth[column])
    
    plt.title("How people get news")
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.gca().spines["left"].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    for column in df.columns:
         first_year = df.index[0]
         plt.scatter(
            first_year,
            df[column][first_year],
            color=colors[column]
        )
         
         plt.text(
            first_year - 0.2,
            df[column][first_year],
            column + ' ' + str(df[column][first_year]) + '%',
            ha='right',
            va='center',
            color=colors[column]
        )

        # Resaltar valores del último año
         last_year = df.index[-1]
         plt.scatter(
            last_year,
            df[column][last_year],
            color=colors[column]
         )

         plt.text(
            last_year + 0.2,
            df[column][last_year],
            str(df[column][last_year]) + '%',
            ha='left',
            va='center',
            color=colors[column]
         )
         plt.tight_layout()


    plt.xticks(df.index, labels=df.index)

    plt.tight_layout()
    os.makedirs(os.path.dirname('files/plots/news.png'), exist_ok=True)
    plt.savefig('files/plots/news.png')
    plt.show()

if __name__ == "__main__":
    pregunta_01()