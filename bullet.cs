using UnityEngine;

public class Bullet : MonoBehaviour
{
    void Start()
    {
        Destroy(gameObject, 3f); // ทำลายหลัง 3 วินาที
    }
}
