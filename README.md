# sml-comfyui-prompt-expansion

Stable Diffusion Prompt Expansion using Deepseek API

- Create API key at https://platform.deepseek.com
- Copy `config.ini.example` to `config.ini` and put the replicate key there. 

## Installation

Navigate to where you have installed ComfyUI. For example:

```shell
cd ~/dev/ComfyUI/
```

Go to the custom nodes folder:

```shell
cd custom_nodes
```

Clone this repo

```shell
git clone https://github.com/smlbiobot/sml-comfyui-prompt-expansion
```

Go inside the repo folder

```shell
cd sml-comfyui-prompt-expansion
```

Install the requirements

```shell
pip install -r requirements.txt
```

Copy the example config `config.ini.example` to `config.ini`, then edit the `config.ini` with the actual Repliate API token.

```shell
cp config.ini.example config.ini
```

Start ComfyUI.
