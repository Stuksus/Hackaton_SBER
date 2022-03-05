{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "MEGQUANT_SBER_MVP.ipynb",
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "Приложение открывается по ссылке из результата последней ячейки: \n",
        "\n",
        "`...`\n",
        "\n",
        "`your url is: ТУТА ССЫЛКА НА ПРИЛОЖЕНИЕ`\n",
        "\n",
        "\n",
        "`...`"
      ],
      "metadata": {
        "id": "yYp6P3t-rezs"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install streamlit -q\n",
        "!pip install streamlit-aggrid \n",
        "!pip install pdpbox"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "yOhfGxSQsgJw",
        "outputId": "b620afce-d102-4d1e-9842-56973464b34b"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[K     |████████████████████████████████| 9.9 MB 5.5 MB/s \n",
            "\u001b[K     |████████████████████████████████| 4.3 MB 45.1 MB/s \n",
            "\u001b[K     |████████████████████████████████| 76 kB 4.8 MB/s \n",
            "\u001b[K     |████████████████████████████████| 181 kB 54.5 MB/s \n",
            "\u001b[K     |████████████████████████████████| 111 kB 57.3 MB/s \n",
            "\u001b[K     |████████████████████████████████| 164 kB 48.6 MB/s \n",
            "\u001b[K     |████████████████████████████████| 63 kB 1.5 MB/s \n",
            "\u001b[K     |████████████████████████████████| 128 kB 51.4 MB/s \n",
            "\u001b[K     |████████████████████████████████| 793 kB 50.3 MB/s \n",
            "\u001b[K     |████████████████████████████████| 380 kB 50.0 MB/s \n",
            "\u001b[?25h  Building wheel for blinker (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "\u001b[31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\n",
            "jupyter-console 5.2.0 requires prompt-toolkit<2.0.0,>=1.0.0, but you have prompt-toolkit 3.0.28 which is incompatible.\n",
            "google-colab 1.0.0 requires ipykernel~=4.10, but you have ipykernel 6.9.1 which is incompatible.\n",
            "google-colab 1.0.0 requires ipython~=5.5.0, but you have ipython 7.32.0 which is incompatible.\u001b[0m\n",
            "Collecting streamlit-aggrid\n",
            "  Downloading streamlit_aggrid-0.2.3.post2-py3-none-any.whl (3.5 MB)\n",
            "\u001b[K     |████████████████████████████████| 3.5 MB 5.3 MB/s \n",
            "\u001b[?25hCollecting simplejson>=3.0\n",
            "  Downloading simplejson-3.17.6-cp37-cp37m-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl (130 kB)\n",
            "\u001b[K     |████████████████████████████████| 130 kB 65.1 MB/s \n",
            "\u001b[?25hRequirement already satisfied: pandas>=1.2 in /usr/local/lib/python3.7/dist-packages (from streamlit-aggrid) (1.3.5)\n",
            "Requirement already satisfied: streamlit>=0.87.0 in /usr/local/lib/python3.7/dist-packages (from streamlit-aggrid) (1.7.0)\n",
            "Collecting python-dotenv<0.20.0,>=0.19.1\n",
            "  Downloading python_dotenv-0.19.2-py2.py3-none-any.whl (17 kB)\n",
            "Requirement already satisfied: python-dateutil>=2.7.3 in /usr/local/lib/python3.7/dist-packages (from pandas>=1.2->streamlit-aggrid) (2.8.2)\n",
            "Requirement already satisfied: numpy>=1.17.3 in /usr/local/lib/python3.7/dist-packages (from pandas>=1.2->streamlit-aggrid) (1.21.5)\n",
            "Requirement already satisfied: pytz>=2017.3 in /usr/local/lib/python3.7/dist-packages (from pandas>=1.2->streamlit-aggrid) (2018.9)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.7/dist-packages (from python-dateutil>=2.7.3->pandas>=1.2->streamlit-aggrid) (1.15.0)\n",
            "Requirement already satisfied: semver in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.87.0->streamlit-aggrid) (2.13.0)\n",
            "Requirement already satisfied: importlib-metadata>=1.4 in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.87.0->streamlit-aggrid) (4.11.2)\n",
            "Requirement already satisfied: click>=7.0 in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.87.0->streamlit-aggrid) (7.1.2)\n",
            "Requirement already satisfied: tzlocal in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.87.0->streamlit-aggrid) (1.5.1)\n",
            "Requirement already satisfied: gitpython!=3.1.19 in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.87.0->streamlit-aggrid) (3.1.27)\n",
            "Requirement already satisfied: cachetools>=4.0 in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.87.0->streamlit-aggrid) (4.2.4)\n",
            "Requirement already satisfied: protobuf!=3.11,>=3.6.0 in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.87.0->streamlit-aggrid) (3.17.3)\n",
            "Requirement already satisfied: pydeck>=0.1.dev5 in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.87.0->streamlit-aggrid) (0.7.1)\n",
            "Requirement already satisfied: base58 in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.87.0->streamlit-aggrid) (2.1.1)\n",
            "Requirement already satisfied: toml in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.87.0->streamlit-aggrid) (0.10.2)\n",
            "Requirement already satisfied: astor in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.87.0->streamlit-aggrid) (0.8.1)\n",
            "Requirement already satisfied: blinker in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.87.0->streamlit-aggrid) (1.4)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.87.0->streamlit-aggrid) (2.23.0)\n",
            "Requirement already satisfied: typing-extensions in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.87.0->streamlit-aggrid) (3.10.0.2)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.87.0->streamlit-aggrid) (21.3)\n",
            "Requirement already satisfied: attrs in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.87.0->streamlit-aggrid) (21.4.0)\n",
            "Requirement already satisfied: pillow>=6.2.0 in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.87.0->streamlit-aggrid) (7.1.2)\n",
            "Requirement already satisfied: pympler>=0.9 in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.87.0->streamlit-aggrid) (1.0.1)\n",
            "Requirement already satisfied: validators in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.87.0->streamlit-aggrid) (0.18.2)\n",
            "Requirement already satisfied: pyarrow in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.87.0->streamlit-aggrid) (6.0.1)\n",
            "Requirement already satisfied: watchdog in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.87.0->streamlit-aggrid) (2.1.6)\n",
            "Requirement already satisfied: tornado>=5.0 in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.87.0->streamlit-aggrid) (5.1.1)\n",
            "Requirement already satisfied: altair>=3.2.0 in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.87.0->streamlit-aggrid) (4.2.0)\n",
            "Requirement already satisfied: entrypoints in /usr/local/lib/python3.7/dist-packages (from altair>=3.2.0->streamlit>=0.87.0->streamlit-aggrid) (0.4)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.7/dist-packages (from altair>=3.2.0->streamlit>=0.87.0->streamlit-aggrid) (0.11.2)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.7/dist-packages (from altair>=3.2.0->streamlit>=0.87.0->streamlit-aggrid) (4.3.3)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.7/dist-packages (from altair>=3.2.0->streamlit>=0.87.0->streamlit-aggrid) (2.11.3)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.7/dist-packages (from gitpython!=3.1.19->streamlit>=0.87.0->streamlit-aggrid) (4.0.9)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.7/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19->streamlit>=0.87.0->streamlit-aggrid) (5.0.0)\n",
            "Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.7/dist-packages (from importlib-metadata>=1.4->streamlit>=0.87.0->streamlit-aggrid) (3.7.0)\n",
            "Requirement already satisfied: importlib-resources>=1.4.0 in /usr/local/lib/python3.7/dist-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit>=0.87.0->streamlit-aggrid) (5.4.0)\n",
            "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /usr/local/lib/python3.7/dist-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit>=0.87.0->streamlit-aggrid) (0.18.1)\n",
            "Requirement already satisfied: ipywidgets>=7.0.0 in /usr/local/lib/python3.7/dist-packages (from pydeck>=0.1.dev5->streamlit>=0.87.0->streamlit-aggrid) (7.6.5)\n",
            "Requirement already satisfied: ipykernel>=5.1.2 in /usr/local/lib/python3.7/dist-packages (from pydeck>=0.1.dev5->streamlit>=0.87.0->streamlit-aggrid) (6.9.1)\n",
            "Requirement already satisfied: traitlets>=4.3.2 in /usr/local/lib/python3.7/dist-packages (from pydeck>=0.1.dev5->streamlit>=0.87.0->streamlit-aggrid) (5.1.1)\n",
            "Requirement already satisfied: matplotlib-inline<0.2.0,>=0.1.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit>=0.87.0->streamlit-aggrid) (0.1.3)\n",
            "Requirement already satisfied: debugpy<2.0,>=1.0.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit>=0.87.0->streamlit-aggrid) (1.0.0)\n",
            "Requirement already satisfied: ipython>=7.23.1 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit>=0.87.0->streamlit-aggrid) (7.32.0)\n",
            "Requirement already satisfied: nest-asyncio in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit>=0.87.0->streamlit-aggrid) (1.5.4)\n",
            "Requirement already satisfied: jupyter-client<8.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit>=0.87.0->streamlit-aggrid) (5.3.5)\n",
            "Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in /usr/local/lib/python3.7/dist-packages (from ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit>=0.87.0->streamlit-aggrid) (3.0.28)\n",
            "Requirement already satisfied: setuptools>=18.5 in /usr/local/lib/python3.7/dist-packages (from ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit>=0.87.0->streamlit-aggrid) (57.4.0)\n",
            "Requirement already satisfied: pexpect>4.3 in /usr/local/lib/python3.7/dist-packages (from ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit>=0.87.0->streamlit-aggrid) (4.8.0)\n",
            "Requirement already satisfied: jedi>=0.16 in /usr/local/lib/python3.7/dist-packages (from ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit>=0.87.0->streamlit-aggrid) (0.18.1)\n",
            "Requirement already satisfied: pygments in /usr/local/lib/python3.7/dist-packages (from ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit>=0.87.0->streamlit-aggrid) (2.6.1)\n",
            "Requirement already satisfied: backcall in /usr/local/lib/python3.7/dist-packages (from ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit>=0.87.0->streamlit-aggrid) (0.2.0)\n",
            "Requirement already satisfied: pickleshare in /usr/local/lib/python3.7/dist-packages (from ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit>=0.87.0->streamlit-aggrid) (0.7.5)\n",
            "Requirement already satisfied: decorator in /usr/local/lib/python3.7/dist-packages (from ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit>=0.87.0->streamlit-aggrid) (4.4.2)\n",
            "Requirement already satisfied: jupyterlab-widgets>=1.0.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=0.87.0->streamlit-aggrid) (1.0.2)\n",
            "Requirement already satisfied: ipython-genutils~=0.2.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=0.87.0->streamlit-aggrid) (0.2.0)\n",
            "Requirement already satisfied: widgetsnbextension~=3.5.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=0.87.0->streamlit-aggrid) (3.5.2)\n",
            "Requirement already satisfied: nbformat>=4.2.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=0.87.0->streamlit-aggrid) (5.1.3)\n",
            "Requirement already satisfied: parso<0.9.0,>=0.8.0 in /usr/local/lib/python3.7/dist-packages (from jedi>=0.16->ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit>=0.87.0->streamlit-aggrid) (0.8.3)\n",
            "Requirement already satisfied: MarkupSafe>=0.23 in /usr/local/lib/python3.7/dist-packages (from jinja2->altair>=3.2.0->streamlit>=0.87.0->streamlit-aggrid) (2.0.1)\n",
            "Requirement already satisfied: jupyter-core>=4.6.0 in /usr/local/lib/python3.7/dist-packages (from jupyter-client<8.0->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit>=0.87.0->streamlit-aggrid) (4.9.2)\n",
            "Requirement already satisfied: pyzmq>=13 in /usr/local/lib/python3.7/dist-packages (from jupyter-client<8.0->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit>=0.87.0->streamlit-aggrid) (22.3.0)\n",
            "Requirement already satisfied: ptyprocess>=0.5 in /usr/local/lib/python3.7/dist-packages (from pexpect>4.3->ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit>=0.87.0->streamlit-aggrid) (0.7.0)\n",
            "Requirement already satisfied: wcwidth in /usr/local/lib/python3.7/dist-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit>=0.87.0->streamlit-aggrid) (0.2.5)\n",
            "Requirement already satisfied: notebook>=4.4.1 in /usr/local/lib/python3.7/dist-packages (from widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=0.87.0->streamlit-aggrid) (5.3.1)\n",
            "Requirement already satisfied: nbconvert in /usr/local/lib/python3.7/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=0.87.0->streamlit-aggrid) (5.6.1)\n",
            "Requirement already satisfied: terminado>=0.8.1 in /usr/local/lib/python3.7/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=0.87.0->streamlit-aggrid) (0.13.1)\n",
            "Requirement already satisfied: Send2Trash in /usr/local/lib/python3.7/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=0.87.0->streamlit-aggrid) (1.8.0)\n",
            "Requirement already satisfied: bleach in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=0.87.0->streamlit-aggrid) (4.1.0)\n",
            "Requirement already satisfied: mistune<2,>=0.8.1 in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=0.87.0->streamlit-aggrid) (0.8.4)\n",
            "Requirement already satisfied: defusedxml in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=0.87.0->streamlit-aggrid) (0.7.1)\n",
            "Requirement already satisfied: testpath in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=0.87.0->streamlit-aggrid) (0.6.0)\n",
            "Requirement already satisfied: pandocfilters>=1.4.1 in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=0.87.0->streamlit-aggrid) (1.5.0)\n",
            "Requirement already satisfied: webencodings in /usr/local/lib/python3.7/dist-packages (from bleach->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=0.87.0->streamlit-aggrid) (0.5.1)\n",
            "Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in /usr/local/lib/python3.7/dist-packages (from packaging->streamlit>=0.87.0->streamlit-aggrid) (3.0.7)\n",
            "Requirement already satisfied: chardet<4,>=3.0.2 in /usr/local/lib/python3.7/dist-packages (from requests->streamlit>=0.87.0->streamlit-aggrid) (3.0.4)\n",
            "Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /usr/local/lib/python3.7/dist-packages (from requests->streamlit>=0.87.0->streamlit-aggrid) (1.24.3)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.7/dist-packages (from requests->streamlit>=0.87.0->streamlit-aggrid) (2021.10.8)\n",
            "Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.7/dist-packages (from requests->streamlit>=0.87.0->streamlit-aggrid) (2.10)\n",
            "Installing collected packages: simplejson, python-dotenv, streamlit-aggrid\n",
            "Successfully installed python-dotenv-0.19.2 simplejson-3.17.6 streamlit-aggrid-0.2.3.post2\n",
            "Collecting pdpbox\n",
            "  Downloading PDPbox-0.2.1.tar.gz (34.0 MB)\n",
            "\u001b[K     |████████████████████████████████| 34.0 MB 154 kB/s \n",
            "\u001b[?25hRequirement already satisfied: pandas in /usr/local/lib/python3.7/dist-packages (from pdpbox) (1.3.5)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.7/dist-packages (from pdpbox) (1.21.5)\n",
            "Requirement already satisfied: scipy in /usr/local/lib/python3.7/dist-packages (from pdpbox) (1.4.1)\n",
            "Requirement already satisfied: joblib in /usr/local/lib/python3.7/dist-packages (from pdpbox) (1.1.0)\n",
            "Requirement already satisfied: psutil in /usr/local/lib/python3.7/dist-packages (from pdpbox) (5.4.8)\n",
            "Collecting matplotlib==3.1.1\n",
            "  Downloading matplotlib-3.1.1-cp37-cp37m-manylinux1_x86_64.whl (13.1 MB)\n",
            "\u001b[K     |████████████████████████████████| 13.1 MB 33.8 MB/s \n",
            "\u001b[?25hRequirement already satisfied: sklearn in /usr/local/lib/python3.7/dist-packages (from pdpbox) (0.0)\n",
            "Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.7/dist-packages (from matplotlib==3.1.1->pdpbox) (0.11.0)\n",
            "Requirement already satisfied: kiwisolver>=1.0.1 in /usr/local/lib/python3.7/dist-packages (from matplotlib==3.1.1->pdpbox) (1.3.2)\n",
            "Requirement already satisfied: python-dateutil>=2.1 in /usr/local/lib/python3.7/dist-packages (from matplotlib==3.1.1->pdpbox) (2.8.2)\n",
            "Requirement already satisfied: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.1 in /usr/local/lib/python3.7/dist-packages (from matplotlib==3.1.1->pdpbox) (3.0.7)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.7/dist-packages (from python-dateutil>=2.1->matplotlib==3.1.1->pdpbox) (1.15.0)\n",
            "Requirement already satisfied: pytz>=2017.3 in /usr/local/lib/python3.7/dist-packages (from pandas->pdpbox) (2018.9)\n",
            "Requirement already satisfied: scikit-learn in /usr/local/lib/python3.7/dist-packages (from sklearn->pdpbox) (1.0.2)\n",
            "Requirement already satisfied: threadpoolctl>=2.0.0 in /usr/local/lib/python3.7/dist-packages (from scikit-learn->sklearn->pdpbox) (3.1.0)\n",
            "Building wheels for collected packages: pdpbox\n",
            "  Building wheel for pdpbox (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for pdpbox: filename=PDPbox-0.2.1-py3-none-any.whl size=35758224 sha256=5f5d058249c16de25ba0378825c437de401087185224e59e3124344e284989a2\n",
            "  Stored in directory: /root/.cache/pip/wheels/f4/d0/1a/b80035625c53131f52906a6fc4dd690d8efd2bf8af6a4015eb\n",
            "Successfully built pdpbox\n",
            "Installing collected packages: matplotlib, pdpbox\n",
            "  Attempting uninstall: matplotlib\n",
            "    Found existing installation: matplotlib 3.2.2\n",
            "    Uninstalling matplotlib-3.2.2:\n",
            "      Successfully uninstalled matplotlib-3.2.2\n",
            "\u001b[31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\n",
            "albumentations 0.1.12 requires imgaug<0.2.7,>=0.2.5, but you have imgaug 0.2.9 which is incompatible.\u001b[0m\n",
            "Successfully installed matplotlib-3.1.1 pdpbox-0.2.1\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "application/vnd.colab-display-data+json": {
              "pip_warning": {
                "packages": [
                  "matplotlib",
                  "mpl_toolkits"
                ]
              }
            }
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "df_test  = pd.read_csv('https://raw.githubusercontent.com/BKHV/risk_models/master/data/PD-data-test.csv', sep=';')\n",
        "df_train = pd.read_csv('https://raw.githubusercontent.com/BKHV/risk_models/master/data/PD-data-train.csv', sep=';')"
      ],
      "metadata": {
        "id": "TmYL4t3gsGnJ"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!streamlit run app.py & npx localtunnel --port 8501"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7T2NnLbrWAwO",
        "outputId": "4180e501-9fd0-43e8-e6b8-a0b0786e4cb0"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2022-03-05 15:32:17.404 INFO    numexpr.utils: NumExpr defaulting to 2 threads.\n",
            "\u001b[0m\n",
            "\u001b[34m\u001b[1m  You can now view your Streamlit app in your browser.\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m  Network URL: \u001b[0m\u001b[1mhttp://172.28.0.2:8501\u001b[0m\n",
            "\u001b[34m  External URL: \u001b[0m\u001b[1mhttp://35.238.203.178:8501\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[K\u001b[?25hnpx: installed 22 in 5.564s\n",
            "your url is: https://fat-parrot-11.loca.lt\n",
            "/usr/local/lib/python3.7/dist-packages/pandas/core/arraylike.py:364: RuntimeWarning:\n",
            "\n",
            "divide by zero encountered in log\n",
            "\n",
            "/usr/local/lib/python3.7/dist-packages/pandas/core/frame.py:9203: FutureWarning:\n",
            "\n",
            "Passing 'suffixes' which cause duplicate columns {'Distr_default_x', 'count_all_x', 'IV_x', 'Distr_non_default_x', 'non_default_x', 'default_x'} in the result is deprecated and will raise a MergeError in a future version.\n",
            "\n",
            "\u001b[34m  Stopping...\u001b[0m\n",
            "^C\n"
          ]
        }
      ]
    }
  ]
}
