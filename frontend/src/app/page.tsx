'use client';
import { useEffect, useState } from 'react';

type QuizQuestion = {
  word: string;
  choices: string[];
  correct_index: number;
};

export default function HomePage() {
  const [question, setQuestion] = useState<QuizQuestion | null>(null);
  const [selected, setSelected] = useState<number | null>(null);
  const [result, setResult] = useState<string>("");

  useEffect(() => {
  fetch('/api/question')
    .then((res) => res.json())
    .then((data: QuizQuestion) => {
      setQuestion(data);
      setSelected(null);
      setResult("");
    })
    .catch((err) => {
      console.error("API取得に失敗しました:", err);
    });
  }, []);


  const handleAnswer = (index: number) => {
    setSelected(index);
    if (index === question?.correct_index) {
      setResult("正解！");
    } else {
      setResult("不正解...");
    }
  };

  return (
    <main className="p-8">
      <h1 className="text-2xl font-bold mb-4">英単語クイズ</h1>
      {question ? (
        <div>
          <p className="mb-2">「{question.word}」の意味は？</p>
          <ul>
            {question.choices.map((choice, idx) => (
              <li key={idx}>
                <button
                  onClick={() => handleAnswer(idx)}
                  className="border p-2 my-1 w-full text-left"
                >
                  {choice}
                </button>
              </li>
            ))}
          </ul>
          {selected !== null && <p className="mt-4">{result}</p>}
        </div>
      ) : (
        <p>問題を読み込み中...</p>
      )}
    </main>
  );
}
