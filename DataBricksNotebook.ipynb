{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "import io\n",
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#btc['CapMrktCurUSD'], btc['AdrActCnt']\n",
    "response = requests.get('https://coinmetrics.io/newdata/btc.csv')\n",
    "file_object = io.StringIO(response.content.decode('utf-8'))\n",
    "btc = pd.read_csv(file_object, index_col=\"date\", parse_dates=[\"date\"], usecols=['CapMrktCurUSD', 'AdrActCnt','date'])\n",
    "btc = btc[\"2013-05-01\":\"2100\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "response = requests.get('https://coinmetrics.io/newdata/eth.csv')\n",
    "file_object = io.StringIO(response.content.decode('utf-8'))\n",
    "eth = pd.read_csv(file_object, index_col=\"date\", parse_dates=[\"date\"])\n",
    "eth = eth[\"2013-05-01\":\"2100\"]\n",
    "eth = eth[np.abs(eth[\"AdrActCnt\"]-eth[\"AdrActCnt\"].mean()) <= (1.5*eth[\"AdrActCnt\"].std())]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "response = requests.get('https://coinmetrics.io/newdata/ltc.csv')\n",
    "file_object = io.StringIO(response.content.decode('utf-8'))\n",
    "ltc = pd.read_csv(file_object, index_col=\"date\", parse_dates=[\"date\"])\n",
    "ltc = ltc[\"2013-05-01\":\"2100\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "btc.to_csv(r'C:\\Users\\mla\\Dev\\cfehome\\AzureDataFactoryDemo\\btc.csv')\n",
    "eth.to_csv(r'C:\\Users\\mla\\Dev\\cfehome\\AzureDataFactoryDemo\\eth.csv')\n",
    "ltc.to_csv(r'C:\\Users\\mla\\Dev\\cfehome\\AzureDataFactoryDemo\\ltc.csv')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
