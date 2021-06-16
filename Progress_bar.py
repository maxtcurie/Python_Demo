from tqdm import tqdm

for i in tqdm(range(100000)):
	i**i

for index, content in enumerate(tqdm(range(100000))):
	content**content