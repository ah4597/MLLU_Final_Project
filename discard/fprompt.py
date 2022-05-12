def text2prompt(text, data_type):
    """Transform from simple input text to hard prompts through manually built templates
    Args:
        text: data including all input x that needed to be transform into prompts, in json format
        data_type: distinguish between conversation words and
    Returns:
        prompts: complete prompts that can be feeded into the model
    """
    prefix_persona = ""
    prefix_ = ""
    for item in data:
        # TODO:
    return prompts
