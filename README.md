
广告的流量覆盖取决于广告的人群定向（匹配对应特征的用户数量）、广告素材尺寸（匹配的广告位）以及投放时段、预算等设置项

影响广告竞争力的主要有出价、广告质量等因素（如 点击率pctr/转化率pcvr 等）以及对用户体验的控制策略

基本竞争力可以用千次曝光收益 epcm

    ecpm = 1000 * cpc_bid * pctr = 1000 * cpa_bid * pctr * pcvr

    其中，cpc, cpa 分别代表按点击付费模式和按转化付费模式。等式1决定广告能参与竞争的次数以及竞争对象，等式2决定在每次竞
争中的胜出概率。二者最终决定广告每天的曝光量。


# totalExposureLog.out
## 历史曝光日志数据文件
### 无缺失值数据，
### bid * pctr + quality_ecpm = totalEpm.  quality_ecpm 可能小于0， 如果 totalEpm 小于1 ，重置为1.0
### 广告请求id  广告位id  广告id的区别?

    1. 广告请求 id：唯一标识每次请求（每个请求对应一个用户某一时刻，可能多个广告位）
    2. 广告请求时间：该字段为时间戳，即 1970 纪元后经过的浮点秒数
    3. 广告位 id：加密后无业务含义，只区分不同广告位，每个广告位只能曝光特定素材尺寸的广告
    4. 用户 id（即看广告的人）：加密后无业务含义，只区分不同用户，可和后面的用户特征数据中 id 相关联
    5. 曝光广告 id：加密后无业务含义，只区分不同广告，可以和广告特征文件中的广告 id 关联
    6. 曝光广告素材尺寸：枚举型取值，不同广告位对素材的尺寸要求不同，同一个广告位可能适配多个不同尺寸的素材
    7. 曝光广告出价 bid：这里只记录 cpc 出价，非 cpc 广告此处记录折算后的 cpc 价格
    8. 曝光广告 pctr：预估的 pctr，和 bid 相乘得到 basic_ecpm
    9. 曝光广告 quality_ecpm：将广告质量和用户体验等因素折算成 ecpm 的分数，主要影响因素有 pctr/pcvr/窄定向等
    10.曝光广告 totalEcpm：广告排序的分数依据，由 basic_ecpm（点击） 和 quality_ecpm（转化） 相加得到



# ad_static_feature.out
## 广告静态数据文件，该类广告属性一般从广告创建后无法修改。所有 id 类数据均为加密后随机映射。
### 素材尺寸可能有多个，商品id可能为空（推广目标为落地页）, 广告行业id可能有多个, 商品id可能有多个

    1. 广告 id：和曝光日志中的广告 id 相关联
    2. 创建时间：广告创建时的时间戳, 可能为0
    3. 广告账户 id：广告所在账户的唯一标识，账户结构分为四级：账户——推广计划——广告——素材
    4. 商品 id：广告推广目标的唯一标识，若推广目标是落地页，则该字段为空
    5. 商品类型：广告推广目标的类型，枚举型
    6. 广告行业 id：广告所属的行业类别标识
    7. 素材尺寸：不同广告位对素材的尺寸要求不同，同一个广告可能有多个不同尺寸的素材，用逗号分隔


# test_sample.dat
## 测试集，由于要评估出价相关性，故测试数据中一条广告 id 会对应多条不同出价的样本。

1. 样本 id
2. 广告 id
3. 创建时间
4. 素材尺寸
5. 广告行业 id
6. 商品类型
7. 商品 id
8. 广告账户 id
9. 投放时段
10. 人群定向
11. 出价（单位分）