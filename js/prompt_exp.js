import { app } from "../../scripts/app.js";

app.registerExtension({
    name: "PromptGeneratorNodeExtension",
    beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeType.comfyClass === "PromptGeneratorNode") {
            const onExecuted = nodeType.prototype.onExecuted;
            nodeType.prototype.onExecuted = function (message) {
                console.log("onExecuted", message);

                onExecuted?.apply(this, arguments);
                const text = message.text.join('');
                for (const widget of this.widgets) {
                    if (widget.name === "output_widget") {
                        widget.value = text;
                    }
                }
            };
        }
    },
});
