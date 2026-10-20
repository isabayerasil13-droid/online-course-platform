# Диаграммы / Диаграммалар

## Общая архитектура / Жалпы сәулет
```mermaid
flowchart TD
  U["Пользователь / Пайдаланушы"] --> WEB["Django: единый проект / Бір жоба"]
  WEB --> ACC["accounts"]
  WEB --> COUR["courses + lessons"]
  WEB --> ENR["enrollments"]
  WEB --> ASG["assignments"]
  WEB --> PR["progress"]
  WEB --> REV["reviews + reports"]
  ACC --> DB[("PostgreSQL")]
  COUR --> DB
  ENR --> DB
  ASG --> DB
  PR --> DB
  REV --> DB
```

## Концептуальная ER-диаграмма / ER диаграммасы
```mermaid
erDiagram
    USER ||--o{ COURSE : teaches
    CATEGORY ||--o{ COURSE : contains
    COURSE ||--o{ LESSON : consists_of
    COURSE ||--o{ ENROLLMENT : receives
    USER ||--o{ ENROLLMENT : enrolls
    LESSON ||--o{ ASSIGNMENT : has
    USER ||--o{ SUBMISSION : sends
    ASSIGNMENT ||--o{ SUBMISSION : receives
    USER ||--o{ PROGRESS : tracks
    LESSON ||--o{ PROGRESS : tracks
    USER {
      int id PK
      string username
      string email
      string role
    }
    CATEGORY {
      int id PK
      string name
    }
    COURSE {
      int id PK
      string title
      int teacher_id FK
      int category_id FK
    }
    LESSON {
      int id PK
      int course_id FK
      string title
      int order
    }
    ENROLLMENT {
      int id PK
      int student_id FK
      int course_id FK
    }
    ASSIGNMENT {
      int id PK
      int lesson_id FK
      int max_score
    }
    SUBMISSION {
      int id PK
      int assignment_id FK
      int student_id FK
      int score
    }
    PROGRESS {
      int id PK
      int student_id FK
      int lesson_id FK
      boolean completed
    }
```

Схема предварительная. Отзывы, комментарии, материалы и конкретная структура тестов будут уточнены при проектировании MVP.

Диаграмма — концептуальная, қазіргі төрт модельдің кестелері жергілікті SQLite дерекқорында жасалды; PostgreSQL-дегі толық схема әлі жоспар ретінде көрсетілген.

Бұл алдын ала жасалған схема. Пікірлер, материалдар және тест құрылымы келесі кезеңде нақтыланады; нақты кестелер әлі жасалған жоқ.
