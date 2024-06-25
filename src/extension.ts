import * as vscode from "vscode";
import { helpGemini } from "./helpGemini";

export function activate(context: vscode.ExtensionContext) {
  console.log('Congratulations, your extension "CodingChecker" is now active!');

  const disposable = vscode.commands.registerCommand(
    "codingchecker.convertToUppercase",
    () => {
      const editor = vscode.window.activeTextEditor;
      if (!editor) {
        vscode.window.showErrorMessage("No active text editor found.");
        return;
      }

      const selection = editor.selection;
      const selectedText = editor.document.getText(selection);
      const convertedText = selectedText.toUpperCase();

      vscode.window.showInformationMessage(`Converted text: ${convertedText}`);
    }
  );

  const helpGeminiDisposable = vscode.commands.registerCommand(
    "codingchecker.helpGemini",
    () => {
      helpGemini();
    }
  );

  context.subscriptions.push(disposable);
  context.subscriptions.push(helpGeminiDisposable);
}

export function deactivate() {}
