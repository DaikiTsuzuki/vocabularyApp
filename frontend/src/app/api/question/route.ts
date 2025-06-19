// frontend/src/app/api/question/route.ts

export async function GET() {
  const res = await fetch('http://localhost:3001/api/question');
  const data = await res.json();
  return Response.json(data);
}
