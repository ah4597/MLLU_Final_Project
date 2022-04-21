import data_utils
import torch

from torch.utils.data import Dataset


class characterDataset(Dataset):
    """
    A torch.utils.data.Dataset wrapper.
    """

    def __init__(self, data, tokenizer, max_seq_length=256):
        """
        Args:
          data: A list containing the data.
          tokenizer: A transformers.PreTrainedTokenizerFast object that is used to
            tokenize the data.
          max_seq_length: Maximum sequence length to either pad or truncate every
            input example to.
        """
        ## Use encode_data() from data_utils to store the input IDs and
        ## attention masks for the data.
        data_processed = data_utils.preprocess(data)
        self.encoded_data = data_utils.encode_data(data_processed,tokenizer,max_seq_length=max_seq_length)


    def __len__(self):
        return len(self.label_list)

    def __getitem__(self, i):
        """
        Returns:
          example: A dictionary containing the input_ids, attention_mask, and
            label for the i-th example, with the values being numeric tensors
            and the keys being 'input_ids', 'attention_mask', and 'labels'.
        """
        ## TODO: Return the i-th example as a dictionary with the keys and values
        ## specified in the function docstring. You should be able to extract the
        ## necessary values from self.encoded_data and self.label_list.
        dic = {}
        dic["input_ids"] = self.encoded_data[0][i]
        dic["attention_mask"] = self.encoded_data[1][i]
        dic["labels"] = self.encoded_data[0][i]
        return dic
