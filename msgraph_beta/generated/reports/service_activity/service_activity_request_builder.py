from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ...models.o_data_errors.o_data_error import ODataError
    from ...models.service_activity import ServiceActivity
    from .get_active_user_metrics_fori_o_s_or_android_mail_by_read_email_with_i_bdccfb21.get_active_user_metrics_fori_o_s_or_android_mail_by_read_email_with_i_0211beb0 import GetActiveUserMetricsForiOSOrAndroidMailByReadEmailWithI_0211beb0
    from .get_active_user_metrics_for_desktop_mail_by_read_email_with_inclus_5945eaac.get_active_user_metrics_for_desktop_mail_by_read_email_with_inclus_5a158a2b import GetActiveUserMetricsForDesktopMailByReadEmailWithInclus_5a158a2b
    from .get_active_user_metrics_for_email_by_modern_authentication_with_i_6b571bd0.get_active_user_metrics_for_email_by_modern_authentication_with_i_df7b7a91 import GetActiveUserMetricsForEmailByModernAuthenticationWithI_df7b7a91
    from .get_active_user_metrics_for_excel_web_with_inclusive_interval_sta_be61b996.get_active_user_metrics_for_excel_web_with_inclusive_interval_sta_120f0d31 import GetActiveUserMetricsForExcelWebWithInclusiveIntervalSta_120f0d31
    from .get_active_user_metrics_for_one_note_web_with_inclusive_interval_s_db52a6d7.get_active_user_metrics_for_one_note_web_with_inclusive_interval_s_07fd4aec import GetActiveUserMetricsForOneNoteWebWithInclusiveIntervalS_07fd4aec
    from .get_active_user_metrics_for_outlook_mac_by_read_email_with_inclusi_d04e48af.get_active_user_metrics_for_outlook_mac_by_read_email_with_inclusi_45d7ecaf import GetActiveUserMetricsForOutlookMacByReadEmailWithInclusi_45d7ecaf
    from .get_active_user_metrics_for_outlook_mobile_by_read_email_with_incl_1fea4fde.get_active_user_metrics_for_outlook_mobile_by_read_email_with_incl_84dc1e81 import GetActiveUserMetricsForOutlookMobileByReadEmailWithIncl_84dc1e81
    from .get_active_user_metrics_for_outlook_web_by_app_opening_with_inclus_794c6e2c.get_active_user_metrics_for_outlook_web_by_app_opening_with_inclus_3ca5bf39 import GetActiveUserMetricsForOutlookWebByAppOpeningWithInclus_3ca5bf39
    from .get_active_user_metrics_for_outlook_web_by_read_email_with_inclusi_5ead6959.get_active_user_metrics_for_outlook_web_by_read_email_with_inclusi_4e2143ff import GetActiveUserMetricsForOutlookWebByReadEmailWithInclusi_4e2143ff
    from .get_active_user_metrics_for_power_point_web_with_inclusive_interv_bc926148.get_active_user_metrics_for_power_point_web_with_inclusive_interv_4095f087 import GetActiveUserMetricsForPowerPointWebWithInclusiveInterv_4095f087
    from .get_active_user_metrics_for_visio_web_with_inclusive_interval_sta_ef4a532b.get_active_user_metrics_for_visio_web_with_inclusive_interval_sta_8d24e942 import GetActiveUserMetricsForVisioWebWithInclusiveIntervalSta_8d24e942
    from .get_active_user_metrics_for_word_web_with_inclusive_interval_star_62c98614.get_active_user_metrics_for_word_web_with_inclusive_interval_star_0b97a62b import GetActiveUserMetricsForWordWebWithInclusiveIntervalStar_0b97a62b
    from .get_audio_streams_over_udp_metrics_for_teams_with_inclusive_inter_127ff88c.get_audio_streams_over_udp_metrics_for_teams_with_inclusive_inter_b37d7783 import GetAudioStreamsOverUdpMetricsForTeamsWithInclusiveInter_b37d7783
    from .get_audio_stream_qo_e_metrics_for_teams_with_inclusive_interval_st_f1693cb9.get_audio_stream_qo_e_metrics_for_teams_with_inclusive_interval_st_f3e1e602 import GetAudioStreamQoEMetricsForTeamsWithInclusiveIntervalSt_f3e1e602
    from .get_connectivity_metrics_for_exchange_with_inclusive_interval_s_d0ab0d41.get_connectivity_metrics_for_exchange_with_inclusive_interval_s_268bd12f import GetConnectivityMetricsForExchangeWithInclusiveIntervalS_268bd12f
    from .get_message_volume_metrics_for_email_delivery_with_inclusive_int_66d025d4.get_message_volume_metrics_for_email_delivery_with_inclusive_int_1166efae import GetMessageVolumeMetricsForEmailDeliveryWithInclusiveInt_1166efae
    from .get_message_volume_metrics_for_teams_chat_with_inclusive_interva_8de3be15.get_message_volume_metrics_for_teams_chat_with_inclusive_interva_3372dced import GetMessageVolumeMetricsForTeamsChatWithInclusiveInterva_3372dced
    from .get_metrics_for_conditional_access_blocked_sign_in_with_inclusiv_e85fac73.get_metrics_for_conditional_access_blocked_sign_in_with_inclusiv_d21ec3fa import GetMetricsForConditionalAccessBlockedSignInWithInclusiv_d21ec3fa
    from .get_metrics_for_conditional_access_compliant_devices_sign_in_suc_9ac34f05.get_metrics_for_conditional_access_compliant_devices_sign_in_suc_2b8eee05 import GetMetricsForConditionalAccessCompliantDevicesSignInSuc_2b8eee05
    from .get_metrics_for_conditional_access_managed_devices_sign_in_succe_89ba2a58.get_metrics_for_conditional_access_managed_devices_sign_in_succe_c8f9e856 import GetMetricsForConditionalAccessManagedDevicesSignInSucce_c8f9e856
    from .get_metrics_for_mfa_sign_in_failure_with_inclusive_interval_start_bd23993d.get_metrics_for_mfa_sign_in_failure_with_inclusive_interval_start_12165a38 import GetMetricsForMfaSignInFailureWithInclusiveIntervalStart_12165a38
    from .get_metrics_for_mfa_sign_in_success_with_inclusive_interval_start_c2f09e85.get_metrics_for_mfa_sign_in_success_with_inclusive_interval_start_bc09247c import GetMetricsForMfaSignInSuccessWithInclusiveIntervalStart_bc09247c
    from .get_metrics_for_network_access_internet_app_policy_allowed_apps_w_d7521871.get_metrics_for_network_access_internet_app_policy_allowed_apps_w_63e7f7cc import GetMetricsForNetworkAccessInternetAppPolicyAllowedAppsW_63e7f7cc
    from .get_metrics_for_network_access_internet_app_policy_allowed_users_381a8906.get_metrics_for_network_access_internet_app_policy_allowed_users_1bd36e40 import GetMetricsForNetworkAccessInternetAppPolicyAllowedUsers_1bd36e40
    from .get_metrics_for_network_access_internet_app_policy_blocked_apps_w_d8ece54f.get_metrics_for_network_access_internet_app_policy_blocked_apps_w_8fa4c5ed import GetMetricsForNetworkAccessInternetAppPolicyBlockedAppsW_8fa4c5ed
    from .get_metrics_for_network_access_internet_app_policy_blocked_users_0fa5a220.get_metrics_for_network_access_internet_app_policy_blocked_users_04d79806 import GetMetricsForNetworkAccessInternetAppPolicyBlockedUsers_04d79806
    from .get_metrics_for_network_access_private_apps_allowed_by_connector_1781beab.get_metrics_for_network_access_private_apps_allowed_by_connector_81890488 import GetMetricsForNetworkAccessPrivateAppsAllowedByConnector_81890488
    from .get_metrics_for_network_access_private_apps_blocked_by_connector_90998d4c.get_metrics_for_network_access_private_apps_blocked_by_connector_be453bc0 import GetMetricsForNetworkAccessPrivateAppsBlockedByConnector_be453bc0
    from .get_metrics_for_network_access_private_app_users_allowed_by_conne_b135c036.get_metrics_for_network_access_private_app_users_allowed_by_conne_432a0138 import GetMetricsForNetworkAccessPrivateAppUsersAllowedByConne_432a0138
    from .get_metrics_for_network_access_private_app_users_blocked_by_conne_28fa2da6.get_metrics_for_network_access_private_app_users_blocked_by_conne_ba1d4d98 import GetMetricsForNetworkAccessPrivateAppUsersBlockedByConne_ba1d4d98
    from .get_metrics_for_network_access_remote_network_branches_alive_wit_7dda565d.get_metrics_for_network_access_remote_network_branches_alive_wit_72bb670e import GetMetricsForNetworkAccessRemoteNetworkBranchesAliveWit_72bb670e
    from .get_metrics_for_network_access_remote_network_branches_b_g_p_conne_5d6ba6d6.get_metrics_for_network_access_remote_network_branches_b_g_p_conne_8c9b4f80 import GetMetricsForNetworkAccessRemoteNetworkBranchesBGPConne_8c9b4f80
    from .get_metrics_for_network_access_remote_network_branches_b_g_p_disco_f79433d8.get_metrics_for_network_access_remote_network_branches_b_g_p_disco_a53b337a import GetMetricsForNetworkAccessRemoteNetworkBranchesBGPDisco_a53b337a
    from .get_metrics_for_network_access_remote_network_branches_tunnel_co_9122597f.get_metrics_for_network_access_remote_network_branches_tunnel_co_b2d2e7b5 import GetMetricsForNetworkAccessRemoteNetworkBranchesTunnelCo_b2d2e7b5
    from .get_metrics_for_network_access_remote_network_branches_tunnel_di_4fdcb75d.get_metrics_for_network_access_remote_network_branches_tunnel_di_aa9c5dda import GetMetricsForNetworkAccessRemoteNetworkBranchesTunnelDi_aa9c5dda
    from .get_metrics_for_saml_sign_in_success_with_inclusive_interval_star_a0a21818.get_metrics_for_saml_sign_in_success_with_inclusive_interval_star_ec7b2074 import GetMetricsForSamlSignInSuccessWithInclusiveIntervalStar_ec7b2074
    from .get_usage_metrics_for_teams_by_launch_with_inclusive_interval_sta_215ae664.get_usage_metrics_for_teams_by_launch_with_inclusive_interval_sta_057fdcb4 import GetUsageMetricsForTeamsByLaunchWithInclusiveIntervalSta_057fdcb4
    from .get_usage_metrics_for_teams_by_meetings_joined_with_inclusive_int_2ed1bee3.get_usage_metrics_for_teams_by_meetings_joined_with_inclusive_int_908050d0 import GetUsageMetricsForTeamsByMeetingsJoinedWithInclusiveInt_908050d0

class ServiceActivityRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the serviceActivity property of the microsoft.graph.reportRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ServiceActivityRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/reports/serviceActivity{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property serviceActivity for reports
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ServiceActivityRequestBuilderGetQueryParameters]] = None) -> Optional[ServiceActivity]:
        """
        Reports that relate to tenant-level authentication activities in Microsoft Entra.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ServiceActivity]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.service_activity import ServiceActivity

        return await self.request_adapter.send_async(request_info, ServiceActivity, error_mapping)
    
    def get_active_user_metrics_for_desktop_mail_by_read_email_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetActiveUserMetricsForDesktopMailByReadEmailWithInclus_5a158a2b:
        """
        Provides operations to call the getActiveUserMetricsForDesktopMailByReadEmail method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetActiveUserMetricsForDesktopMailByReadEmailWithInclus_5a158a2b
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_active_user_metrics_for_desktop_mail_by_read_email_with_inclus_5945eaac.get_active_user_metrics_for_desktop_mail_by_read_email_with_inclus_5a158a2b import GetActiveUserMetricsForDesktopMailByReadEmailWithInclus_5a158a2b

        return GetActiveUserMetricsForDesktopMailByReadEmailWithInclus_5a158a2b(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_active_user_metrics_for_email_by_modern_authentication_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetActiveUserMetricsForEmailByModernAuthenticationWithI_df7b7a91:
        """
        Provides operations to call the getActiveUserMetricsForEmailByModernAuthentication method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetActiveUserMetricsForEmailByModernAuthenticationWithI_df7b7a91
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_active_user_metrics_for_email_by_modern_authentication_with_i_6b571bd0.get_active_user_metrics_for_email_by_modern_authentication_with_i_df7b7a91 import GetActiveUserMetricsForEmailByModernAuthenticationWithI_df7b7a91

        return GetActiveUserMetricsForEmailByModernAuthenticationWithI_df7b7a91(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_active_user_metrics_for_excel_web_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetActiveUserMetricsForExcelWebWithInclusiveIntervalSta_120f0d31:
        """
        Provides operations to call the getActiveUserMetricsForExcelWeb method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetActiveUserMetricsForExcelWebWithInclusiveIntervalSta_120f0d31
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_active_user_metrics_for_excel_web_with_inclusive_interval_sta_be61b996.get_active_user_metrics_for_excel_web_with_inclusive_interval_sta_120f0d31 import GetActiveUserMetricsForExcelWebWithInclusiveIntervalSta_120f0d31

        return GetActiveUserMetricsForExcelWebWithInclusiveIntervalSta_120f0d31(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_active_user_metrics_for_one_note_web_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetActiveUserMetricsForOneNoteWebWithInclusiveIntervalS_07fd4aec:
        """
        Provides operations to call the getActiveUserMetricsForOneNoteWeb method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetActiveUserMetricsForOneNoteWebWithInclusiveIntervalS_07fd4aec
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_active_user_metrics_for_one_note_web_with_inclusive_interval_s_db52a6d7.get_active_user_metrics_for_one_note_web_with_inclusive_interval_s_07fd4aec import GetActiveUserMetricsForOneNoteWebWithInclusiveIntervalS_07fd4aec

        return GetActiveUserMetricsForOneNoteWebWithInclusiveIntervalS_07fd4aec(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_active_user_metrics_for_outlook_mac_by_read_email_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetActiveUserMetricsForOutlookMacByReadEmailWithInclusi_45d7ecaf:
        """
        Provides operations to call the getActiveUserMetricsForOutlookMacByReadEmail method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetActiveUserMetricsForOutlookMacByReadEmailWithInclusi_45d7ecaf
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_active_user_metrics_for_outlook_mac_by_read_email_with_inclusi_d04e48af.get_active_user_metrics_for_outlook_mac_by_read_email_with_inclusi_45d7ecaf import GetActiveUserMetricsForOutlookMacByReadEmailWithInclusi_45d7ecaf

        return GetActiveUserMetricsForOutlookMacByReadEmailWithInclusi_45d7ecaf(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_active_user_metrics_for_outlook_mobile_by_read_email_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetActiveUserMetricsForOutlookMobileByReadEmailWithIncl_84dc1e81:
        """
        Provides operations to call the getActiveUserMetricsForOutlookMobileByReadEmail method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetActiveUserMetricsForOutlookMobileByReadEmailWithIncl_84dc1e81
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_active_user_metrics_for_outlook_mobile_by_read_email_with_incl_1fea4fde.get_active_user_metrics_for_outlook_mobile_by_read_email_with_incl_84dc1e81 import GetActiveUserMetricsForOutlookMobileByReadEmailWithIncl_84dc1e81

        return GetActiveUserMetricsForOutlookMobileByReadEmailWithIncl_84dc1e81(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_active_user_metrics_for_outlook_web_by_app_opening_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetActiveUserMetricsForOutlookWebByAppOpeningWithInclus_3ca5bf39:
        """
        Provides operations to call the getActiveUserMetricsForOutlookWebByAppOpening method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetActiveUserMetricsForOutlookWebByAppOpeningWithInclus_3ca5bf39
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_active_user_metrics_for_outlook_web_by_app_opening_with_inclus_794c6e2c.get_active_user_metrics_for_outlook_web_by_app_opening_with_inclus_3ca5bf39 import GetActiveUserMetricsForOutlookWebByAppOpeningWithInclus_3ca5bf39

        return GetActiveUserMetricsForOutlookWebByAppOpeningWithInclus_3ca5bf39(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_active_user_metrics_for_outlook_web_by_read_email_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetActiveUserMetricsForOutlookWebByReadEmailWithInclusi_4e2143ff:
        """
        Provides operations to call the getActiveUserMetricsForOutlookWebByReadEmail method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetActiveUserMetricsForOutlookWebByReadEmailWithInclusi_4e2143ff
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_active_user_metrics_for_outlook_web_by_read_email_with_inclusi_5ead6959.get_active_user_metrics_for_outlook_web_by_read_email_with_inclusi_4e2143ff import GetActiveUserMetricsForOutlookWebByReadEmailWithInclusi_4e2143ff

        return GetActiveUserMetricsForOutlookWebByReadEmailWithInclusi_4e2143ff(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_active_user_metrics_for_power_point_web_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetActiveUserMetricsForPowerPointWebWithInclusiveInterv_4095f087:
        """
        Provides operations to call the getActiveUserMetricsForPowerPointWeb method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetActiveUserMetricsForPowerPointWebWithInclusiveInterv_4095f087
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_active_user_metrics_for_power_point_web_with_inclusive_interv_bc926148.get_active_user_metrics_for_power_point_web_with_inclusive_interv_4095f087 import GetActiveUserMetricsForPowerPointWebWithInclusiveInterv_4095f087

        return GetActiveUserMetricsForPowerPointWebWithInclusiveInterv_4095f087(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_active_user_metrics_for_visio_web_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetActiveUserMetricsForVisioWebWithInclusiveIntervalSta_8d24e942:
        """
        Provides operations to call the getActiveUserMetricsForVisioWeb method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetActiveUserMetricsForVisioWebWithInclusiveIntervalSta_8d24e942
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_active_user_metrics_for_visio_web_with_inclusive_interval_sta_ef4a532b.get_active_user_metrics_for_visio_web_with_inclusive_interval_sta_8d24e942 import GetActiveUserMetricsForVisioWebWithInclusiveIntervalSta_8d24e942

        return GetActiveUserMetricsForVisioWebWithInclusiveIntervalSta_8d24e942(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_active_user_metrics_for_word_web_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetActiveUserMetricsForWordWebWithInclusiveIntervalStar_0b97a62b:
        """
        Provides operations to call the getActiveUserMetricsForWordWeb method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetActiveUserMetricsForWordWebWithInclusiveIntervalStar_0b97a62b
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_active_user_metrics_for_word_web_with_inclusive_interval_star_62c98614.get_active_user_metrics_for_word_web_with_inclusive_interval_star_0b97a62b import GetActiveUserMetricsForWordWebWithInclusiveIntervalStar_0b97a62b

        return GetActiveUserMetricsForWordWebWithInclusiveIntervalStar_0b97a62b(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_active_user_metrics_fori_o_s_or_android_mail_by_read_email_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetActiveUserMetricsForiOSOrAndroidMailByReadEmailWithI_0211beb0:
        """
        Provides operations to call the getActiveUserMetricsForiOSOrAndroidMailByReadEmail method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetActiveUserMetricsForiOSOrAndroidMailByReadEmailWithI_0211beb0
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_active_user_metrics_fori_o_s_or_android_mail_by_read_email_with_i_bdccfb21.get_active_user_metrics_fori_o_s_or_android_mail_by_read_email_with_i_0211beb0 import GetActiveUserMetricsForiOSOrAndroidMailByReadEmailWithI_0211beb0

        return GetActiveUserMetricsForiOSOrAndroidMailByReadEmailWithI_0211beb0(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_audio_stream_qo_e_metrics_for_teams_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetAudioStreamQoEMetricsForTeamsWithInclusiveIntervalSt_f3e1e602:
        """
        Provides operations to call the getAudioStreamQoEMetricsForTeams method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetAudioStreamQoEMetricsForTeamsWithInclusiveIntervalSt_f3e1e602
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_audio_stream_qo_e_metrics_for_teams_with_inclusive_interval_st_f1693cb9.get_audio_stream_qo_e_metrics_for_teams_with_inclusive_interval_st_f3e1e602 import GetAudioStreamQoEMetricsForTeamsWithInclusiveIntervalSt_f3e1e602

        return GetAudioStreamQoEMetricsForTeamsWithInclusiveIntervalSt_f3e1e602(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_audio_streams_over_udp_metrics_for_teams_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetAudioStreamsOverUdpMetricsForTeamsWithInclusiveInter_b37d7783:
        """
        Provides operations to call the getAudioStreamsOverUdpMetricsForTeams method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetAudioStreamsOverUdpMetricsForTeamsWithInclusiveInter_b37d7783
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_audio_streams_over_udp_metrics_for_teams_with_inclusive_inter_127ff88c.get_audio_streams_over_udp_metrics_for_teams_with_inclusive_inter_b37d7783 import GetAudioStreamsOverUdpMetricsForTeamsWithInclusiveInter_b37d7783

        return GetAudioStreamsOverUdpMetricsForTeamsWithInclusiveInter_b37d7783(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_connectivity_metrics_for_exchange_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetConnectivityMetricsForExchangeWithInclusiveIntervalS_268bd12f:
        """
        Provides operations to call the getConnectivityMetricsForExchange method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetConnectivityMetricsForExchangeWithInclusiveIntervalS_268bd12f
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_connectivity_metrics_for_exchange_with_inclusive_interval_s_d0ab0d41.get_connectivity_metrics_for_exchange_with_inclusive_interval_s_268bd12f import GetConnectivityMetricsForExchangeWithInclusiveIntervalS_268bd12f

        return GetConnectivityMetricsForExchangeWithInclusiveIntervalS_268bd12f(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_message_volume_metrics_for_email_delivery_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetMessageVolumeMetricsForEmailDeliveryWithInclusiveInt_1166efae:
        """
        Provides operations to call the getMessageVolumeMetricsForEmailDelivery method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetMessageVolumeMetricsForEmailDeliveryWithInclusiveInt_1166efae
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_message_volume_metrics_for_email_delivery_with_inclusive_int_66d025d4.get_message_volume_metrics_for_email_delivery_with_inclusive_int_1166efae import GetMessageVolumeMetricsForEmailDeliveryWithInclusiveInt_1166efae

        return GetMessageVolumeMetricsForEmailDeliveryWithInclusiveInt_1166efae(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_message_volume_metrics_for_teams_chat_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetMessageVolumeMetricsForTeamsChatWithInclusiveInterva_3372dced:
        """
        Provides operations to call the getMessageVolumeMetricsForTeamsChat method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetMessageVolumeMetricsForTeamsChatWithInclusiveInterva_3372dced
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_message_volume_metrics_for_teams_chat_with_inclusive_interva_8de3be15.get_message_volume_metrics_for_teams_chat_with_inclusive_interva_3372dced import GetMessageVolumeMetricsForTeamsChatWithInclusiveInterva_3372dced

        return GetMessageVolumeMetricsForTeamsChatWithInclusiveInterva_3372dced(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_metrics_for_conditional_access_blocked_sign_in_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetMetricsForConditionalAccessBlockedSignInWithInclusiv_d21ec3fa:
        """
        Provides operations to call the getMetricsForConditionalAccessBlockedSignIn method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetMetricsForConditionalAccessBlockedSignInWithInclusiv_d21ec3fa
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_metrics_for_conditional_access_blocked_sign_in_with_inclusiv_e85fac73.get_metrics_for_conditional_access_blocked_sign_in_with_inclusiv_d21ec3fa import GetMetricsForConditionalAccessBlockedSignInWithInclusiv_d21ec3fa

        return GetMetricsForConditionalAccessBlockedSignInWithInclusiv_d21ec3fa(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_metrics_for_conditional_access_compliant_devices_sign_in_success_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetMetricsForConditionalAccessCompliantDevicesSignInSuc_2b8eee05:
        """
        Provides operations to call the getMetricsForConditionalAccessCompliantDevicesSignInSuccess method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetMetricsForConditionalAccessCompliantDevicesSignInSuc_2b8eee05
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_metrics_for_conditional_access_compliant_devices_sign_in_suc_9ac34f05.get_metrics_for_conditional_access_compliant_devices_sign_in_suc_2b8eee05 import GetMetricsForConditionalAccessCompliantDevicesSignInSuc_2b8eee05

        return GetMetricsForConditionalAccessCompliantDevicesSignInSuc_2b8eee05(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_metrics_for_conditional_access_managed_devices_sign_in_success_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetMetricsForConditionalAccessManagedDevicesSignInSucce_c8f9e856:
        """
        Provides operations to call the getMetricsForConditionalAccessManagedDevicesSignInSuccess method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetMetricsForConditionalAccessManagedDevicesSignInSucce_c8f9e856
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_metrics_for_conditional_access_managed_devices_sign_in_succe_89ba2a58.get_metrics_for_conditional_access_managed_devices_sign_in_succe_c8f9e856 import GetMetricsForConditionalAccessManagedDevicesSignInSucce_c8f9e856

        return GetMetricsForConditionalAccessManagedDevicesSignInSucce_c8f9e856(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_metrics_for_mfa_sign_in_failure_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetMetricsForMfaSignInFailureWithInclusiveIntervalStart_12165a38:
        """
        Provides operations to call the getMetricsForMfaSignInFailure method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetMetricsForMfaSignInFailureWithInclusiveIntervalStart_12165a38
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_metrics_for_mfa_sign_in_failure_with_inclusive_interval_start_bd23993d.get_metrics_for_mfa_sign_in_failure_with_inclusive_interval_start_12165a38 import GetMetricsForMfaSignInFailureWithInclusiveIntervalStart_12165a38

        return GetMetricsForMfaSignInFailureWithInclusiveIntervalStart_12165a38(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_metrics_for_mfa_sign_in_success_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetMetricsForMfaSignInSuccessWithInclusiveIntervalStart_bc09247c:
        """
        Provides operations to call the getMetricsForMfaSignInSuccess method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetMetricsForMfaSignInSuccessWithInclusiveIntervalStart_bc09247c
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_metrics_for_mfa_sign_in_success_with_inclusive_interval_start_c2f09e85.get_metrics_for_mfa_sign_in_success_with_inclusive_interval_start_bc09247c import GetMetricsForMfaSignInSuccessWithInclusiveIntervalStart_bc09247c

        return GetMetricsForMfaSignInSuccessWithInclusiveIntervalStart_bc09247c(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_metrics_for_network_access_internet_app_policy_allowed_apps_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetMetricsForNetworkAccessInternetAppPolicyAllowedAppsW_63e7f7cc:
        """
        Provides operations to call the getMetricsForNetworkAccessInternetAppPolicyAllowedApps method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetMetricsForNetworkAccessInternetAppPolicyAllowedAppsW_63e7f7cc
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_metrics_for_network_access_internet_app_policy_allowed_apps_w_d7521871.get_metrics_for_network_access_internet_app_policy_allowed_apps_w_63e7f7cc import GetMetricsForNetworkAccessInternetAppPolicyAllowedAppsW_63e7f7cc

        return GetMetricsForNetworkAccessInternetAppPolicyAllowedAppsW_63e7f7cc(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_metrics_for_network_access_internet_app_policy_allowed_users_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetMetricsForNetworkAccessInternetAppPolicyAllowedUsers_1bd36e40:
        """
        Provides operations to call the getMetricsForNetworkAccessInternetAppPolicyAllowedUsers method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetMetricsForNetworkAccessInternetAppPolicyAllowedUsers_1bd36e40
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_metrics_for_network_access_internet_app_policy_allowed_users_381a8906.get_metrics_for_network_access_internet_app_policy_allowed_users_1bd36e40 import GetMetricsForNetworkAccessInternetAppPolicyAllowedUsers_1bd36e40

        return GetMetricsForNetworkAccessInternetAppPolicyAllowedUsers_1bd36e40(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_metrics_for_network_access_internet_app_policy_blocked_apps_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetMetricsForNetworkAccessInternetAppPolicyBlockedAppsW_8fa4c5ed:
        """
        Provides operations to call the getMetricsForNetworkAccessInternetAppPolicyBlockedApps method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetMetricsForNetworkAccessInternetAppPolicyBlockedAppsW_8fa4c5ed
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_metrics_for_network_access_internet_app_policy_blocked_apps_w_d8ece54f.get_metrics_for_network_access_internet_app_policy_blocked_apps_w_8fa4c5ed import GetMetricsForNetworkAccessInternetAppPolicyBlockedAppsW_8fa4c5ed

        return GetMetricsForNetworkAccessInternetAppPolicyBlockedAppsW_8fa4c5ed(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_metrics_for_network_access_internet_app_policy_blocked_users_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetMetricsForNetworkAccessInternetAppPolicyBlockedUsers_04d79806:
        """
        Provides operations to call the getMetricsForNetworkAccessInternetAppPolicyBlockedUsers method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetMetricsForNetworkAccessInternetAppPolicyBlockedUsers_04d79806
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_metrics_for_network_access_internet_app_policy_blocked_users_0fa5a220.get_metrics_for_network_access_internet_app_policy_blocked_users_04d79806 import GetMetricsForNetworkAccessInternetAppPolicyBlockedUsers_04d79806

        return GetMetricsForNetworkAccessInternetAppPolicyBlockedUsers_04d79806(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_metrics_for_network_access_private_app_users_allowed_by_connector_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetMetricsForNetworkAccessPrivateAppUsersAllowedByConne_432a0138:
        """
        Provides operations to call the getMetricsForNetworkAccessPrivateAppUsersAllowedByConnector method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetMetricsForNetworkAccessPrivateAppUsersAllowedByConne_432a0138
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_metrics_for_network_access_private_app_users_allowed_by_conne_b135c036.get_metrics_for_network_access_private_app_users_allowed_by_conne_432a0138 import GetMetricsForNetworkAccessPrivateAppUsersAllowedByConne_432a0138

        return GetMetricsForNetworkAccessPrivateAppUsersAllowedByConne_432a0138(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_metrics_for_network_access_private_app_users_blocked_by_connector_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetMetricsForNetworkAccessPrivateAppUsersBlockedByConne_ba1d4d98:
        """
        Provides operations to call the getMetricsForNetworkAccessPrivateAppUsersBlockedByConnector method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetMetricsForNetworkAccessPrivateAppUsersBlockedByConne_ba1d4d98
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_metrics_for_network_access_private_app_users_blocked_by_conne_28fa2da6.get_metrics_for_network_access_private_app_users_blocked_by_conne_ba1d4d98 import GetMetricsForNetworkAccessPrivateAppUsersBlockedByConne_ba1d4d98

        return GetMetricsForNetworkAccessPrivateAppUsersBlockedByConne_ba1d4d98(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_metrics_for_network_access_private_apps_allowed_by_connector_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetMetricsForNetworkAccessPrivateAppsAllowedByConnector_81890488:
        """
        Provides operations to call the getMetricsForNetworkAccessPrivateAppsAllowedByConnector method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetMetricsForNetworkAccessPrivateAppsAllowedByConnector_81890488
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_metrics_for_network_access_private_apps_allowed_by_connector_1781beab.get_metrics_for_network_access_private_apps_allowed_by_connector_81890488 import GetMetricsForNetworkAccessPrivateAppsAllowedByConnector_81890488

        return GetMetricsForNetworkAccessPrivateAppsAllowedByConnector_81890488(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_metrics_for_network_access_private_apps_blocked_by_connector_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetMetricsForNetworkAccessPrivateAppsBlockedByConnector_be453bc0:
        """
        Provides operations to call the getMetricsForNetworkAccessPrivateAppsBlockedByConnector method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetMetricsForNetworkAccessPrivateAppsBlockedByConnector_be453bc0
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_metrics_for_network_access_private_apps_blocked_by_connector_90998d4c.get_metrics_for_network_access_private_apps_blocked_by_connector_be453bc0 import GetMetricsForNetworkAccessPrivateAppsBlockedByConnector_be453bc0

        return GetMetricsForNetworkAccessPrivateAppsBlockedByConnector_be453bc0(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_metrics_for_network_access_remote_network_branches_alive_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetMetricsForNetworkAccessRemoteNetworkBranchesAliveWit_72bb670e:
        """
        Provides operations to call the getMetricsForNetworkAccessRemoteNetworkBranchesAlive method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetMetricsForNetworkAccessRemoteNetworkBranchesAliveWit_72bb670e
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_metrics_for_network_access_remote_network_branches_alive_wit_7dda565d.get_metrics_for_network_access_remote_network_branches_alive_wit_72bb670e import GetMetricsForNetworkAccessRemoteNetworkBranchesAliveWit_72bb670e

        return GetMetricsForNetworkAccessRemoteNetworkBranchesAliveWit_72bb670e(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_metrics_for_network_access_remote_network_branches_b_g_p_connected_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetMetricsForNetworkAccessRemoteNetworkBranchesBGPConne_8c9b4f80:
        """
        Provides operations to call the getMetricsForNetworkAccessRemoteNetworkBranchesBGPConnected method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetMetricsForNetworkAccessRemoteNetworkBranchesBGPConne_8c9b4f80
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_metrics_for_network_access_remote_network_branches_b_g_p_conne_5d6ba6d6.get_metrics_for_network_access_remote_network_branches_b_g_p_conne_8c9b4f80 import GetMetricsForNetworkAccessRemoteNetworkBranchesBGPConne_8c9b4f80

        return GetMetricsForNetworkAccessRemoteNetworkBranchesBGPConne_8c9b4f80(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_metrics_for_network_access_remote_network_branches_b_g_p_disconnected_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetMetricsForNetworkAccessRemoteNetworkBranchesBGPDisco_a53b337a:
        """
        Provides operations to call the getMetricsForNetworkAccessRemoteNetworkBranchesBGPDisconnected method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetMetricsForNetworkAccessRemoteNetworkBranchesBGPDisco_a53b337a
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_metrics_for_network_access_remote_network_branches_b_g_p_disco_f79433d8.get_metrics_for_network_access_remote_network_branches_b_g_p_disco_a53b337a import GetMetricsForNetworkAccessRemoteNetworkBranchesBGPDisco_a53b337a

        return GetMetricsForNetworkAccessRemoteNetworkBranchesBGPDisco_a53b337a(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_metrics_for_network_access_remote_network_branches_tunnel_connected_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetMetricsForNetworkAccessRemoteNetworkBranchesTunnelCo_b2d2e7b5:
        """
        Provides operations to call the getMetricsForNetworkAccessRemoteNetworkBranchesTunnelConnected method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetMetricsForNetworkAccessRemoteNetworkBranchesTunnelCo_b2d2e7b5
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_metrics_for_network_access_remote_network_branches_tunnel_co_9122597f.get_metrics_for_network_access_remote_network_branches_tunnel_co_b2d2e7b5 import GetMetricsForNetworkAccessRemoteNetworkBranchesTunnelCo_b2d2e7b5

        return GetMetricsForNetworkAccessRemoteNetworkBranchesTunnelCo_b2d2e7b5(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_metrics_for_network_access_remote_network_branches_tunnel_disconnected_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetMetricsForNetworkAccessRemoteNetworkBranchesTunnelDi_aa9c5dda:
        """
        Provides operations to call the getMetricsForNetworkAccessRemoteNetworkBranchesTunnelDisconnected method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetMetricsForNetworkAccessRemoteNetworkBranchesTunnelDi_aa9c5dda
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_metrics_for_network_access_remote_network_branches_tunnel_di_4fdcb75d.get_metrics_for_network_access_remote_network_branches_tunnel_di_aa9c5dda import GetMetricsForNetworkAccessRemoteNetworkBranchesTunnelDi_aa9c5dda

        return GetMetricsForNetworkAccessRemoteNetworkBranchesTunnelDi_aa9c5dda(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_metrics_for_saml_sign_in_success_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetMetricsForSamlSignInSuccessWithInclusiveIntervalStar_ec7b2074:
        """
        Provides operations to call the getMetricsForSamlSignInSuccess method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetMetricsForSamlSignInSuccessWithInclusiveIntervalStar_ec7b2074
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_metrics_for_saml_sign_in_success_with_inclusive_interval_star_a0a21818.get_metrics_for_saml_sign_in_success_with_inclusive_interval_star_ec7b2074 import GetMetricsForSamlSignInSuccessWithInclusiveIntervalStar_ec7b2074

        return GetMetricsForSamlSignInSuccessWithInclusiveIntervalStar_ec7b2074(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_usage_metrics_for_teams_by_launch_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetUsageMetricsForTeamsByLaunchWithInclusiveIntervalSta_057fdcb4:
        """
        Provides operations to call the getUsageMetricsForTeamsByLaunch method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetUsageMetricsForTeamsByLaunchWithInclusiveIntervalSta_057fdcb4
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_usage_metrics_for_teams_by_launch_with_inclusive_interval_sta_215ae664.get_usage_metrics_for_teams_by_launch_with_inclusive_interval_sta_057fdcb4 import GetUsageMetricsForTeamsByLaunchWithInclusiveIntervalSta_057fdcb4

        return GetUsageMetricsForTeamsByLaunchWithInclusiveIntervalSta_057fdcb4(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    def get_usage_metrics_for_teams_by_meetings_joined_with_inclusive_interval_start_date_time_with_exclusive_interval_end_date_time_with_aggregation_interval_in_minutes(self,exclusive_interval_end_date_time: datetime.datetime, inclusive_interval_start_date_time: datetime.datetime) -> GetUsageMetricsForTeamsByMeetingsJoinedWithInclusiveInt_908050d0:
        """
        Provides operations to call the getUsageMetricsForTeamsByMeetingsJoined method.
        param exclusive_interval_end_date_time: Usage: exclusiveIntervalEndDateTime={exclusiveIntervalEndDateTime}
        param inclusive_interval_start_date_time: Usage: inclusiveIntervalStartDateTime={inclusiveIntervalStartDateTime}
        Returns: GetUsageMetricsForTeamsByMeetingsJoinedWithInclusiveInt_908050d0
        """
        if exclusive_interval_end_date_time is None:
            raise TypeError("exclusive_interval_end_date_time cannot be null.")
        if inclusive_interval_start_date_time is None:
            raise TypeError("inclusive_interval_start_date_time cannot be null.")
        from .get_usage_metrics_for_teams_by_meetings_joined_with_inclusive_int_2ed1bee3.get_usage_metrics_for_teams_by_meetings_joined_with_inclusive_int_908050d0 import GetUsageMetricsForTeamsByMeetingsJoinedWithInclusiveInt_908050d0

        return GetUsageMetricsForTeamsByMeetingsJoinedWithInclusiveInt_908050d0(self.request_adapter, self.path_parameters, exclusive_interval_end_date_time, inclusive_interval_start_date_time)
    
    async def patch(self,body: ServiceActivity, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ServiceActivity]:
        """
        Update the navigation property serviceActivity in reports
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ServiceActivity]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.service_activity import ServiceActivity

        return await self.request_adapter.send_async(request_info, ServiceActivity, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property serviceActivity for reports
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ServiceActivityRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Reports that relate to tenant-level authentication activities in Microsoft Entra.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: ServiceActivity, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property serviceActivity in reports
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> ServiceActivityRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ServiceActivityRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ServiceActivityRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ServiceActivityRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ServiceActivityRequestBuilderGetQueryParameters():
        """
        Reports that relate to tenant-level authentication activities in Microsoft Entra.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[list[str]] = None

        # Select properties to be returned
        select: Optional[list[str]] = None

    
    @dataclass
    class ServiceActivityRequestBuilderGetRequestConfiguration(RequestConfiguration[ServiceActivityRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ServiceActivityRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

