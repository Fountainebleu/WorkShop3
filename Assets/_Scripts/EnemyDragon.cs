using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using Random = UnityEngine.Random;
using SimpleJSON;


public class EnemyDragon : MonoBehaviour
{
    public GameObject dragonEggPrefab;
    public float speed = 1;
    public float timeBetweenEggDrops = 1f;
    public float leftRightDistance = 10f;
    public float chanceDirection = 0.1f;
    private LevelManager levelManager;
    
    void Start()
    {
        levelManager = GameObject.Find("LevelManager").GetComponent<LevelManager>();
        StartCoroutine(GoogleSheets());
        Invoke("DropEgg", 2f);
    }

    IEnumerator GoogleSheets()
    {
        var url =
            "https://sheets.googleapis.com/v4/spreadsheets/1AWIzQIQIJpiYiGZp7hzbYT2hgNwW152vB1AbJE1aX-o/values/A2:E11?key=AIzaSyCo6uB0fxKN7kmr77Z5xhPSQ0vs0abXIg4";
        UnityWebRequest request = UnityWebRequest.Get(url);
        yield return request.SendWebRequest();

        if (request.result == UnityWebRequest.Result.Success)
        {
            var jsonData = JSON.Parse(request.downloadHandler.text);
            var values = jsonData["values"];
            for (int i = 0; i < values.Count; i++)
            {
                var row = values[i];
                var level = int.Parse(row[0]);
                if (level == levelManager.currentLevel)
                {
                    speed = float.Parse(row[1]);
                    timeBetweenEggDrops = float.Parse(row[2]);
                    chanceDirection = float.Parse(row[3]);
                    leftRightDistance = float.Parse(row[4]);
                    Debug.Log($"Данные уровня {level}: Speed={speed}, TimeBetweenEggDrops={timeBetweenEggDrops}, ChanceDirection={chanceDirection}, LeftRightDistance={leftRightDistance}");
                    break;
                }
            }
        }
        else
        {
            Debug.LogError("Ошибка загрузки: " + request.error);
        }
    }
    
    void DropEgg(){
        Vector3 myVector = new Vector3(0.0f, 5.0f, 0.0f);
        GameObject egg = Instantiate<GameObject>(dragonEggPrefab);
        egg.transform.position = transform.position + myVector;
        Invoke("DropEgg", timeBetweenEggDrops);
    }

    // Update is called once per frame
    void Update()
    {
        Vector3 pos = transform.position;
        pos.x += speed * Time.deltaTime;
        transform.position = pos;

        if (pos.x < -leftRightDistance){
            speed = Mathf.Abs(speed);
        }
        else if (pos.x > leftRightDistance){
            speed = -Mathf.Abs(speed);
        }
    }

    private void FixedUpdate() {
        if (Random.value < chanceDirection){
            speed *= -1;
        }
    }
}
