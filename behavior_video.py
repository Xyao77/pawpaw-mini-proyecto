import random

BEHAVIOR_LIBRARY = {
    "Stretching": {
        "zh": {
            "Cute": [
                "我来松松骨头啦～",
                "先拉伸一下，我要开机了。",
                "睡醒先活动活动🐾"
            ],
            "Attitude": [
                "身体先热个机。",
                "今天先从舒展开始。",
                "别急，我在进入状态。"
            ],
            "meanings": [
                "刚睡醒后活动身体",
                "让身体放松一下",
                "准备开始动起来",
                "一种自然的舒展动作"
            ]
        },
        "es": {
            "Cute": [
                "vale, toca estirarse un poco",
                "primero me activo y luego hablamos",
                "recien despierto... dame un segundo"
            ],
            "Attitude": [
                "estoy entrando en modo funcional",
                "primero me organizo el cuerpo",
                "hoy empezamos con estilo"
            ],
            "meanings": [
                "Activar el cuerpo después de descansar",
                "Relajar los músculos",
                "Prepararse para moverse",
                "Movimiento natural de estiramiento"
            ]
        },
        "en": {
            "Cute": [
                "okay, time for a little stretch",
                "let me wake up properly first",
                "just stretching a bit"
            ],
            "Attitude": [
                "starting the day correctly",
                "body first, chaos later",
                "warming up in style"
            ],
            "meanings": [
                "Waking up and activating the body",
                "Relaxing the muscles",
                "Getting ready to move",
                "A natural stretching behavior"
            ]
        }
    },

    "Yawning": {
        "zh": {
            "Cute": [
                "我有点困啦…",
                "我刚睡醒，先缓缓。",
                "哈欠打完再说😴"
            ],
            "Attitude": [
                "今天先低电量运行。",
                "我还没完全开机。",
                "先让我加载一下。"
            ],
            "meanings": [
                "有点困",
                "刚睡醒",
                "身体正在放松",
                "有时也可能是轻微紧张释放"
            ]
        },
        "es": {
            "Cute": [
                "tengo sueño, no me metas prisa",
                "acabo de despertarme, dame un segundo",
                "primero bostezo y luego veo"
            ],
            "Attitude": [
                "todavia no estoy operativo",
                "hoy voy con bateria baja",
                "estoy cargando sistema"
            ],
            "meanings": [
                "Sueño",
                "Recién despertado",
                "Relajación",
                "A veces también libera tensión"
            ]
        },
        "en": {
            "Cute": [
                "i’m still sleepy...",
                "i literally just woke up",
                "let me yawn first"
            ],
            "Attitude": [
                "still booting up",
                "running on low battery today",
                "system not fully online yet"
            ],
            "meanings": [
                "Sleepiness",
                "Just waking up",
                "Relaxation",
                "Sometimes mild tension release"
            ]
        }
    },

    "Rolling": {
        "zh": {
            "Cute": [
                "快来陪我玩嘛！！",
                "我今天心情超好噜～",
                "看到我打滚没？快夸我！"
            ],
            "Attitude": [
                "本狗今天状态拉满。",
                "看我这波操作。",
                "我现在就是全场焦点。"
            ],
            "meanings": [
                "心情很好",
                "想玩耍",
                "在放松自己",
                "在吸引你的注意"
            ]
        },
        "es": {
            "Cute": [
                "mirame que guapo",
                "hoy soy puro amor",
                "asi de feliz estoy"
            ],
            "Attitude": [
                "nivel de ternura: maximo",
                "yo hoy: paz total",
                "soy literalmente arte"
            ],
            "meanings": [
                "Buen estado de ánimo",
                "Ganas de jugar",
                "Relajación",
                "Búsqueda de atención"
            ]
        },
        "en": {
            "Cute": [
                "look at me, i’m adorable",
                "today i’m pure joy",
                "this is peak happiness"
            ],
            "Attitude": [
                "i’m literally art",
                "main character energy",
                "i am the moment"
            ],
            "meanings": [
                "Good mood",
                "Playfulness",
                "Relaxation",
                "Attention-seeking"
            ]
        }
    },

    "Airplane ears": {
        "zh": {
            "Cute": [
                "我有一点点心虚…",
                "你先别凶我嘛…",
                "我先低调一下。"
            ],
            "Attitude": [
                "我现在先安静观察。",
                "今天先不高调。",
                "局势有点微妙。"
            ],
            "meanings": [
                "有点紧张",
                "在表达服从",
                "有点心虚",
                "社交上有些不确定"
            ]
        },
        "es": {
            "Cute": [
                "vale... mejor me porto bien",
                "no me mires asi",
                "yo ahora mismo, perfil bajo"
            ],
            "Attitude": [
                "estoy leyendo la situacion",
                "hoy mejor no destacar",
                "voy a mantener perfil bajo"
            ],
            "meanings": [
                "Nerviosismo",
                "Sumisión",
                "Ligera culpa corporal",
                "Inseguridad social"
            ]
        },
        "en": {
            "Cute": [
                "okay... i’ll behave",
                "please don’t look at me like that",
                "keeping a low profile right now"
            ],
            "Attitude": [
                "reading the room",
                "not drawing attention today",
                "staying subtle for now"
            ],
            "meanings": [
                "Nervousness",
                "Submission",
                "Mild guilt-like body language",
                "Social uncertainty"
            ]
        }
    },

    "Spinning": {
        "zh": {
            "Cute": [
                "我要出去玩啦！！！",
                "快快快，我准备好啦！",
                "我兴奋得都转圈圈了～～"
            ],
            "Attitude": [
                "出门，现在。",
                "我已经准备好了。",
                "别让我等太久。"
            ],
            "meanings": [
                "对外出很兴奋",
                "充满期待",
                "精力很高",
                "对固定日常流程有反应"
            ]
        },
        "es": {
            "Cute": [
                "quiero salir yaaa",
                "vamos, que estoy listo",
                "no puedo parar quieto"
            ],
            "Attitude": [
                "salir. ya.",
                "llevo listo desde hace rato",
                "no me hagas esperar"
            ],
            "meanings": [
                "Emoción por salir",
                "Anticipación",
                "Mucha energía",
                "Rutina aprendida antes del paseo"
            ]
        },
        "en": {
            "Cute": [
                "i wanna go out now!!",
                "come on, i’m ready already!",
                "i’m too excited to stay still"
            ],
            "Attitude": [
                "walk. now.",
                "i’ve been ready",
                "don’t keep me waiting"
            ],
            "meanings": [
                "Excitement before going out",
                "Anticipation",
                "High energy",
                "Learned walk/play routine"
            ]
        }
    },

    "Running toward owner": {
        "zh": {
            "Cute": [
                "我来噜！！",
                "我冲过来找你啦～",
                "看到你我就忍不住啦！"
            ],
            "Attitude": [
                "目标锁定：你。",
                "我直接冲刺过来。",
                "看到你就得立刻出现。"
            ],
            "meanings": [
                "在热情打招呼",
                "非常兴奋",
                "想靠近主人",
                "在寻求互动"
            ]
        },
        "es": {
            "Cute": [
                "ya voy ya voy",
                "voy corriendo hacia ti",
                "te he visto y he venido directo"
            ],
            "Attitude": [
                "objetivo detectado: tu",
                "voy directo sin escalas",
                "te veo y aparezco"
            ],
            "meanings": [
                "Saludo",
                "Emoción",
                "Vínculo con el dueño",
                "Búsqueda de interacción"
            ]
        },
        "en": {
            "Cute": [
                "here i come!!",
                "i ran straight to you!",
                "the second i saw you, i came over"
            ],
            "Attitude": [
                "target locked: you",
                "zero hesitation, full sprint",
                "i see you, i appear"
            ],
            "meanings": [
                "Greeting behavior",
                "Excitement",
                "Attachment to owner",
                "Seeking interaction"
            ]
        }
    },

    "Tail tucked": {
        "zh": {
            "Cute": [
                "我错啦…别凶我嘛",
                "我先低调一点…",
                "这次真的不是故意的啦…"
            ],
            "Attitude": [
                "我现在很安静。",
                "今天先不高调。",
                "我先观察一下局势。"
            ],
            "meanings": [
                "有些害怕",
                "表达服从",
                "有点焦虑",
                "缺乏安全感"
            ]
        },
        "es": {
            "Cute": [
                "vale... creo que la lie",
                "yo mejor me quedo quietecito",
                "ups... creo que hice algo mal"
            ],
            "Attitude": [
                "ahora mismo, perfil bajo",
                "hoy mejor no llamar la atencion",
                "estoy leyendo la situacion"
            ],
            "meanings": [
                "Miedo",
                "Sumisión",
                "Ansiedad",
                "Inseguridad"
            ]
        },
        "en": {
            "Cute": [
                "okay... i think i messed up",
                "i’ll just stay very still now",
                "oops... i may have done something wrong"
            ],
            "Attitude": [
                "low profile mode",
                "not drawing attention today",
                "i’m reading the room"
            ],
            "meanings": [
                "Fear",
                "Submission",
                "Anxiety",
                "Insecurity"
            ]
        }
    },

    "Sitting still": {
        "zh": {
            "Cute": [
                "我在等你先开口。",
                "我现在只是静静地美丽。",
                "你是不是已经被我迷住了？"
            ],
            "Attitude": [
                "人类，你也很为我着迷吧。",
                "我不动，也足够有存在感。",
                "高级感，不需要动作。"
            ],
            "meanings": [
                "在观察环境",
                "在等待互动",
                "暂时比较平静",
                "也可能只是单纯在发呆"
            ]
        },
        "es": {
            "Cute": [
                "estoy esperando a que hables primero",
                "yo aqui, simplemente siendo precioso",
                "te has quedado mirandome, eh"
            ],
            "Attitude": [
                "humano, tambien estas obsesionado conmigo, verdad",
                "sin moverme ya llamo la atencion",
                "presencia. sin esfuerzo."
            ],
            "meanings": [
                "Observación del entorno",
                "Esperando interacción",
                "Estado tranquilo",
                "O simplemente pensando en nada"
            ]
        },
        "en": {
            "Cute": [
                "i’m waiting for you to speak first",
                "just sitting here being adorable",
                "you’re staring at me again, huh"
            ],
            "Attitude": [
                "human, you’re obsessed with me too, right",
                "i don’t even need to move",
                "presence. no effort."
            ],
            "meanings": [
                "Observing the environment",
                "Waiting for interaction",
                "Calm state",
                "Or just zoning out"
            ]
        }
    },

    "Head tilt": {
        "zh": {
            "Cute": [
                "你刚刚说什么呀？",
                "我在认真听你讲话哦。",
                "你是不是在叫我宝贝？"
            ],
            "Attitude": [
                "你这话，值得我思考一下。",
                "我对你的人类行为产生了兴趣。",
                "你成功引起了我的注意。"
            ],
            "meanings": [
                "对声音或人类讲话感兴趣",
                "在尝试理解信息",
                "对互动有反应",
                "表现出好奇心"
            ]
        },
        "es": {
            "Cute": [
                "que acabas de decir",
                "te estoy escuchando eh",
                "me has llamado guapo?"
            ],
            "Attitude": [
                "interesante... continua",
                "has captado mi atencion",
                "tu comportamiento humano me intriga"
            ],
            "meanings": [
                "Interés por sonidos o voz humana",
                "Intento de comprender",
                "Respuesta a interacción",
                "Curiosidad"
            ]
        },
        "en": {
            "Cute": [
                "wait, what did you just say",
                "i’m listening very carefully",
                "did you just call me cute"
            ],
            "Attitude": [
                "interesting... go on",
                "you have my attention now",
                "your human behavior intrigues me"
            ],
            "meanings": [
                "Interest in sound or speech",
                "Trying to understand",
                "Response to interaction",
                "Curiosity"
            ]
        }
    },

    "Tongue out (cute)": {
        "zh": {
            "Cute": [
                "我是不是超可爱？",
                "今天走甜妹路线～",
                "我这样是不是犯规了？"
            ],
            "Attitude": [
                "萌这件事，我是专业的。",
                "别装了，你已经被我拿下了。",
                "我知道我很会。"
            ],
            "meanings": [
                "放松状态",
                "有点卖萌",
                "表情比较轻松",
                "可能只是自然吐舌"
            ]
        },
        "es": {
            "Cute": [
                "soy demasiado mono y lo sabes",
                "hoy voy en modo tierno",
                "esto ya es ilegal de lo adorable"
            ],
            "Attitude": [
                "ser adorable es mi profesion",
                "ya te he conquistado",
                "yo se perfectamente lo que hago"
            ],
            "meanings": [
                "Estado relajado",
                "Expresión tierna",
                "Lenguaje corporal suave",
                "O simplemente gesto natural"
            ]
        },
        "en": {
            "Cute": [
                "i’m way too cute and you know it",
                "today i’m in soft mode",
                "this level of adorable should be illegal"
            ],
            "Attitude": [
                "being adorable is my profession",
                "i already won you over",
                "i know exactly what i’m doing"
            ],
            "meanings": [
                "Relaxed state",
                "Cute expression",
                "Soft body language",
                "Or just a natural gesture"
            ]
        }
    },

    "Tongue out (hot)": {
        "zh": {
            "Cute": [
                "我有点热啦…",
                "先散散热再继续玩。",
                "今天太阳有点太努力了。"
            ],
            "Attitude": [
                "我现在进入高温模式。",
                "请立刻给我空调待遇。",
                "这天气对本狗不友好。"
            ],
            "meanings": [
                "觉得热",
                "在通过喘气散热",
                "运动后体温升高",
                "需要注意补水和休息"
            ]
        },
        "es": {
            "Cute": [
                "vale, hace un poquito demasiado calor",
                "primero me refresco y luego seguimos",
                "hoy el sol va fuerte eh"
            ],
            "Attitude": [
                "modo calor activado",
                "exijo aire acondicionado inmediatamente",
                "este clima no esta hecho para mi"
            ],
            "meanings": [
                "Sensación de calor",
                "Jadeo para regular temperatura",
                "Temperatura elevada tras actividad",
                "Conviene descansar e hidratar"
            ]
        },
        "en": {
            "Cute": [
                "okay, it’s kinda too hot",
                "let me cool down first",
                "the sun is doing too much today"
            ],
            "Attitude": [
                "heat mode activated",
                "i demand air conditioning immediately",
                "this weather is not for me"
            ],
            "meanings": [
                "Feeling hot",
                "Panting to cool down",
                "Body temperature elevated after activity",
                "Needs hydration and rest"
            ]
        }
    },

    "Smiling / Grinning": {
        "zh": {
            "Cute": [
                "我今天心情很好哦。",
                "看到你我就忍不住笑啦。",
                "我这样是不是很治愈？"
            ],
            "Attitude": [
                "今天由我负责可爱。",
                "微笑，是我的基本礼仪。",
                "你看到的是高级营业状态。"
            ],
            "meanings": [
                "状态放松",
                "可能感到开心",
                "表情友好",
                "也可能只是嘴型碰巧像微笑"
            ]
        },
        "es": {
            "Cute": [
                "hoy estoy de muy buen humor",
                "te veo y ya se me nota",
                "esto es sonrisa premium"
            ],
            "Attitude": [
                "hoy me toca ser encantador",
                "sonreir es parte de mi marca",
                "esto no es una sonrisa, es presencia"
            ],
            "meanings": [
                "Estado relajado",
                "Posible emoción positiva",
                "Expresión amistosa",
                "A veces también es simplemente la forma de la boca"
            ]
        },
        "en": {
            "Cute": [
                "i’m in such a good mood today",
                "i saw you and instantly smiled",
                "this is premium cuteness"
            ],
            "Attitude": [
                "being charming is part of my brand",
                "this isn’t a smile, it’s presence",
                "today i’m serving face"
            ],
            "meanings": [
                "Relaxed state",
                "Possible positive emotion",
                "Friendly expression",
                "Sometimes it’s just natural mouth shape"
            ]
        }
    },

    "Showing teeth": {
        "zh": {
            "Cute": [
                "你先别误会我啦…",
                "我这个表情有点复杂。",
                "我也不知道为什么长这样。"
            ],
            "Attitude": [
                "我现在情绪有点立体。",
                "这不是普通表情管理。",
                "请谨慎解读本狗神情。"
            ],
            "meanings": [
                "可能是紧张或防御",
                "也可能只是特殊表情",
                "需要结合耳朵尾巴等整体判断",
                "不要只看牙齿下结论"
            ]
        },
        "es": {
            "Cute": [
                "vale, no lo interpretes mal",
                "mi expresion hoy esta un poco intensa",
                "yo tampoco se por que he puesto esta cara"
            ],
            "Attitude": [
                "mi lenguaje corporal hoy es complejo",
                "esto requiere analisis avanzado",
                "no saques conclusiones tan rapido"
            ],
            "meanings": [
                "Puede indicar tensión o defensa",
                "O simplemente una expresión rara",
                "Conviene observar cola, orejas y contexto",
                "No interpretar solo por los dientes"
            ]
        },
        "en": {
            "Cute": [
                "okay, don’t take this the wrong way",
                "my face is doing something weird today",
                "i’m not even sure why i look like this"
            ],
            "Attitude": [
                "my body language today is layered",
                "this requires advanced analysis",
                "do not jump to conclusions"
            ],
            "meanings": [
                "May indicate tension or defensiveness",
                "Or just an unusual expression",
                "Should be interpreted with tail/ears/context",
                "Do not judge based on teeth alone"
            ]
        }
    },

    "Poop spin / crouch": {
        "zh": {
            "Cute": [
                "先别看我，我在办正事。",
                "这是我的仪式感时刻。",
                "等我一下，我马上回来。"
            ],
            "Attitude": [
                "请给我一点私人空间。",
                "现在进入严肃流程。",
                "本狗正在处理人生大事。"
            ],
            "meanings": [
                "可能在找合适位置排便",
                "属于常见如厕前行为",
                "有时会先转圈确认环境",
                "属于正常日常行为之一"
            ]
        },
        "es": {
            "Cute": [
                "un momento, estoy ocupadito",
                "esto requiere concentracion",
                "ahora vuelvo, estoy en algo importante"
            ],
            "Attitude": [
                "necesito privacidad inmediatamente",
                "entrando en modo asunto serio",
                "estoy gestionando temas importantes"
            ],
            "meanings": [
                "Búsqueda de lugar adecuado para defecar",
                "Comportamiento común antes de hacer caca",
                "A veces gira para comprobar el entorno",
                "Parte del comportamiento cotidiano"
            ]
        },
        "en": {
            "Cute": [
                "give me a second, i’m busy",
                "this requires focus",
                "i’ll be right back, i’m handling something important"
            ],
            "Attitude": [
                "privacy. immediately.",
                "entering serious business mode",
                "currently handling important matters"
            ],
            "meanings": [
                "Looking for a place to poop",
                "Common pre-toilet behavior",
                "May spin first to check surroundings",
                "A normal daily routine behavior"
            ]
        }
    },

    "Thinking pose": {
        "zh": {
            "Cute": [
                "我在思考狗生。",
                "别打扰，我脑子在转。",
                "我现在有点哲学。"
            ],
            "Attitude": [
                "本狗正在进行深度思考。",
                "这是高级脑内活动。",
                "有些事情，值得我认真考虑。"
            ],
            "meanings": [
                "在观察",
                "在等待信息",
                "看起来比较专注",
                "也可能只是刚好停住了"
            ]
        },
        "es": {
            "Cute": [
                "estoy pensando en la vida",
                "no me interrumpas, estoy procesando",
                "hoy estoy filosofico"
            ],
            "Attitude": [
                "analisis profundo en curso",
                "esto es actividad cerebral avanzada",
                "hay cosas que merecen mi reflexion"
            ],
            "meanings": [
                "Observación",
                "Esperando información",
                "Estado de atención",
                "O simplemente pausa momentánea"
            ]
        },
        "en": {
            "Cute": [
                "i’m thinking about life",
                "don’t interrupt, i’m processing",
                "feeling philosophical today"
            ],
            "Attitude": [
                "deep analysis in progress",
                "advanced brain activity happening",
                "some things deserve my reflection"
            ],
            "meanings": [
                "Observing",
                "Waiting for information",
                "Focused state",
                "Or simply pausing for a moment"
            ]
        }
    },

    "Sleeping": {
        "zh": {
            "Cute": [
                "先别吵，我睡得正香呢。",
                "本狗现在进入省电模式。",
                "睡觉也是我的正事。"
            ],
            "Attitude": [
                "今天谁都别想打扰我。",
                "高级休眠中。",
                "我现在只负责睡得很有质感。"
            ],
            "meanings": [
                "正在休息或补觉",
                "身体处于放松状态",
                "可能在恢复精力",
                "属于日常正常行为"
            ]
        },
        "es": {
            "Cute": [
                "shhh, estoy durmiendo super bien",
                "ahora mismo estoy en modo ahorro de energia",
                "dormir tambien es una tarea importante"
            ],
            "Attitude": [
                "hoy no molestar",
                "descanso premium en proceso",
                "estoy durmiendo con muchisimo estilo"
            ],
            "meanings": [
                "Descanso o sueño",
                "Estado de relajación",
                "Recuperación de energía",
                "Comportamiento cotidiano normal"
            ]
        },
        "en": {
            "Cute": [
                "shhh, i’m sleeping so well",
                "currently in power-saving mode",
                "sleeping is also an important task"
            ],
            "Attitude": [
                "do not disturb today",
                "premium rest in progress",
                "i’m sleeping with exceptional style"
            ],
            "meanings": [
                "Resting or sleeping",
                "Relaxed state",
                "Recovering energy",
                "A normal daily behavior"
            ]
        }
    },
    "Toy": {
    "zh": {
        "Cute": [
            "这是我的宝贝！",
            "今天我要一直抱着它。",
            "谁都别想拿走我的玩具。"
        ],
        "Attitude": [
            "这个玩具现在归我。",
            "今天我和它锁死了。",
            "别碰，这是我的战利品。"
        ],
        "meanings": [
            "对玩具很感兴趣",
            "想玩耍或已经进入玩耍状态",
            "对某个物品有明显注意力",
            "可能处于兴奋或放松的互动状态"
        ]
    },
    "es": {
        "Cute": [
            "este juguete es mío",
            "hoy no me separo de esto",
            "nadie toca mi tesoro"
        ],
        "Attitude": [
            "esto me pertenece",
            "mi juguete, mis reglas",
            "no intentes quitármelo"
        ],
        "meanings": [
            "Interés por un juguete",
            "Estado de juego o anticipación de juego",
            "Fijación en un objeto",
            "Puede indicar emoción o interacción relajada"
        ]
    },
    "en": {
        "Cute": [
            "this toy is mine",
            "i’m not letting go of this today",
            "nobody touches my treasure"
        ],
        "Attitude": [
            "this belongs to me",
            "my toy, my rules",
            "don’t even try to take it"
        ],
        "meanings": [
            "Interest in a toy",
            "Playful state or anticipation of play",
            "Focused attention on an object",
            "May indicate excitement or relaxed interaction"
        ]
    }
},

    "Other / Mystery": {
        "zh": {
            "Cute": [
                "你猜不透我～",
                "我有我自己的节奏。",
                "你先别急着下定义。"
            ],
            "Attitude": [
                "本狗行为学，禁止乱猜。",
                "这是高级操作。",
                "你们人类不懂。"
            ],
            "meanings": [
                "行为比较难归类",
                "可能和个体性格有关",
                "需要结合场景理解",
                "人类暂时还没看懂"
            ]
        },
        "es": {
            "Cute": [
                "no intentes entenderme",
                "voy a mi rollo",
                "tengo mis propios planes"
            ],
            "Attitude": [
                "demasiado complejo para humanos",
                "esto esta fuera de vuestro nivel",
                "mi mente va por libre"
            ],
            "meanings": [
                "Comportamiento difícil de clasificar",
                "Puede depender de la personalidad",
                "Necesita contexto",
                "El humano todavía no lo entiende"
            ]
        },
        "en": {
            "Cute": [
                "don’t even try to figure me out",
                "i’m on my own little vibe",
                "i’ve got my own plans"
            ],
            "Attitude": [
                "too complex for humans",
                "beyond your understanding",
                "my mind works differently"
            ],
            "meanings": [
                "Behavior is hard to classify",
                "May depend on personality",
                "Needs more context",
                "Human still confused"
            ]
        }
    }
}


LANGUAGE_MAP = {
    "中文": "zh",
    "Español": "es",
    "English": "en"
}


def clean_tts_text(text, language):
    replacements = {
        "zh": {
            "૮₍ ˃ ⤙ ˂ ₎ა": "",
            "🐾": "",
            "😴": "",
            "…": "，",
            "！！": "！",
            "～～": "～"
        },
        "es": {
            "🐾": "",
            "😌": "",
            "😔": "",
            "…": ", ",
            "¡": "",
            "¿": ""
        },
        "en": {
            "🐾": "",
            "😌": "",
            "😴": "",
            "...": ", "
        }
    }

    lang_code = LANGUAGE_MAP.get(language, "en")
    cleaned = text

    for old, new in replacements.get(lang_code, {}).items():
        cleaned = cleaned.replace(old, new)

    return cleaned.strip()


def generate_behavior_text(behavior, language, style):
    lang_code = LANGUAGE_MAP.get(language, "en")
    behavior_data = BEHAVIOR_LIBRARY.get(behavior, BEHAVIOR_LIBRARY["Other / Mystery"])
    lang_data = behavior_data.get(lang_code, behavior_data["en"])

    if style in lang_data:
        subtitle_line = random.choice(lang_data[style])
    else:
        subtitle_line = random.choice(lang_data["Cute"])

    tts_line = clean_tts_text(subtitle_line, language)
    meanings = lang_data["meanings"]

    hook_map = {
        "zh": {
            "Stretching": "刚睡醒的我",
            "Yawning": "还没完全开机",
            "Rolling": "本狗今日状态",
            "Airplane ears": "被抓包的时候",
            "Spinning": "知道要出门的我",
            "Running toward owner": "看到你的那一刻",
            "Tail tucked": "我好像闯祸了",
            "Sitting still": "安静的时候也很迷人",
            "Head tilt": "我在认真听你讲话",
            "Tongue out (cute)": "今日可爱营业中",
            "Tongue out (hot)": "热到小舌头都出来了",
            "Smiling / Grinning": "今天心情真的不错",
            "Showing teeth": "这个表情有点复杂",
            "Poop spin / crouch": "现在在办正事",
            "Thinking pose": "本狗正在思考狗生",
            "Sleeping": "本狗正在高质量休眠",
            "Other / Mystery": "你猜不透我"
        },
        "es": {
            "Stretching": "recien despierto",
            "Yawning": "todavia cargando sistema",
            "Rolling": "mi mood de hoy",
            "Airplane ears": "cuando me pillan",
            "Spinning": "cuando se que vamos a salir",
            "Running toward owner": "en cuanto te veo",
            "Tail tucked": "creo que la lie",
            "Sitting still": "mi presencia ya hace suficiente",
            "Head tilt": "cuando intento entenderte",
            "Tongue out (cute)": "modo adorable activado",
            "Tongue out (hot)": "hace demasiado calor hoy",
            "Smiling / Grinning": "hoy me toca sonreir",
            "Showing teeth": "esto requiere contexto",
            "Poop spin / crouch": "asunto serio en proceso",
            "Thinking pose": "pensamientos profundos",
            "Sleeping": "descanso premium",
            "Other / Mystery": "no intentes entenderme"
        },
        "en": {
            "Stretching": "just woke up",
            "Yawning": "still loading",
            "Rolling": "today's mood",
            "Airplane ears": "when I get caught",
            "Spinning": "when I know we're going out",
            "Running toward owner": "the moment I see you",
            "Tail tucked": "I think I messed up",
            "Sitting still": "being iconic without moving",
            "Head tilt": "when I’m trying to understand you",
            "Tongue out (cute)": "cute mode activated",
            "Tongue out (hot)": "it is way too hot today",
            "Smiling / Grinning": "good mood detected",
            "Showing teeth": "this expression needs context",
            "Poop spin / crouch": "serious business mode",
            "Thinking pose": "deep thoughts happening",
            "Sleeping": "premium rest mode",
            "Other / Mystery": "you'll never understand me"
        }
    }

    hook_line = hook_map.get(lang_code, hook_map["en"]).get(
        behavior,
        hook_map.get(lang_code, hook_map["en"])["Other / Mystery"]
    )

    result = f"""
## What your pet would say
{subtitle_line}

## Mood
- {style}

## What it might mean
- {meanings[0]}
- {meanings[1]}
- {meanings[2]}
- {meanings[3]}
"""
    return result, hook_line, subtitle_line, tts_line