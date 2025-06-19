use axum::{
    routing::get,
    Json, Router,
};
use serde::Serialize;
use std::net::SocketAddr;
use tokio::net::TcpListener; // ← New!

#[derive(Serialize)]
struct QuizQuestion {
    word: String,
    choices: Vec<String>,
    correct_index: usize,
}

async fn get_question() -> Json<QuizQuestion> {
    let question = QuizQuestion {
        word: "apple".to_string(),
        choices: vec![
            "りんご".to_string(),
            "みかん".to_string(),
            "バナナ".to_string(),
            "ぶどう".to_string(),
        ],
        correct_index: 0,
    };
    Json(question)
}

#[tokio::main]
async fn main() {
    let app = Router::new().route("/api/question", get(get_question));

    let listener = TcpListener::bind("127.0.0.1:3001").await.unwrap();
    println!("🚀 Listening on http://{}", listener.local_addr().unwrap());

    axum::serve(listener, app).await.unwrap();  // ← 修正済み
}
