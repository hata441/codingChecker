import * as vscode from "vscode";
import * as ENV from "./env";
import { GoogleGenerativeAI } from "@google/generative-ai";

export function helpGemini() {
  const editor = vscode.window.activeTextEditor;
  if (!editor) {
    vscode.window.showErrorMessage("No active text editor found.");
    return;
  }

  const selection = editor.selection;
  const selectedText = editor.document.getText(selection);
  const text = connectGemini(`${JUMON}\n${selectedText}`);
  vscode.window.showInformationMessage(
    `親愛なるあなたへ。\n${text}\n以上、Geminiより`
  );
}

async function connectGemini(request: string) {
  const genAI = new GoogleGenerativeAI(ENV.GEMINI_INFO.API_KEY);
  const model = genAI.getGenerativeModel({ model: "gemini-pro" });
  const result = await model.generateContent(request);
  const response = await result.response;
  return response.text();
}

const JUMON = "回答は日本語でお願いします。";
