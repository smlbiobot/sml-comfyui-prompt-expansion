import { app } from "../../scripts/app.js";

app.registerExtension({
    name: "com.seeminglee.PromptGeneratorNodeExtension",

    async beforeRegisterNodeDef(nodeType, nodeData, app) {

        if (nodeType.comfyClass === "SML_Prompt_Generator") {
            const onExecuted = nodeType.prototype.onExecuted;

            nodeType.prototype.onExecuted = function (message) {
                onExecuted?.apply(this, arguments);
                const text = message.output_widget.join('');
                for (const widget of this.widgets) {
                    if (widget.name === "output_widget") {
                        widget.value = text;
                    }
                }
            };
        }
    },
});
