from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

delivery_optimization_bandwidth = lazy_import('msgraph.generated.models.delivery_optimization_bandwidth')
delivery_optimization_group_id_source = lazy_import('msgraph.generated.models.delivery_optimization_group_id_source')
delivery_optimization_max_cache_size = lazy_import('msgraph.generated.models.delivery_optimization_max_cache_size')
delivery_optimization_restrict_peer_selection_by_options = lazy_import('msgraph.generated.models.delivery_optimization_restrict_peer_selection_by_options')
device_configuration = lazy_import('msgraph.generated.models.device_configuration')
enablement = lazy_import('msgraph.generated.models.enablement')
windows_delivery_optimization_mode = lazy_import('msgraph.generated.models.windows_delivery_optimization_mode')

class WindowsDeliveryOptimizationConfiguration(device_configuration.DeviceConfiguration):
    @property
    def background_download_from_http_delay_in_seconds(self,) -> Optional[int]:
        """
        Gets the backgroundDownloadFromHttpDelayInSeconds property value. Specifies number of seconds to delay an HTTP source in a background download that is allowed to use peer-to-peer. Valid values 0 to 4294967295
        Returns: Optional[int]
        """
        return self._background_download_from_http_delay_in_seconds
    
    @background_download_from_http_delay_in_seconds.setter
    def background_download_from_http_delay_in_seconds(self,value: Optional[int] = None) -> None:
        """
        Sets the backgroundDownloadFromHttpDelayInSeconds property value. Specifies number of seconds to delay an HTTP source in a background download that is allowed to use peer-to-peer. Valid values 0 to 4294967295
        Args:
            value: Value to set for the backgroundDownloadFromHttpDelayInSeconds property.
        """
        self._background_download_from_http_delay_in_seconds = value
    
    @property
    def bandwidth_mode(self,) -> Optional[delivery_optimization_bandwidth.DeliveryOptimizationBandwidth]:
        """
        Gets the bandwidthMode property value. Specifies foreground and background bandwidth usage using percentages, absolutes, or hours.
        Returns: Optional[delivery_optimization_bandwidth.DeliveryOptimizationBandwidth]
        """
        return self._bandwidth_mode
    
    @bandwidth_mode.setter
    def bandwidth_mode(self,value: Optional[delivery_optimization_bandwidth.DeliveryOptimizationBandwidth] = None) -> None:
        """
        Sets the bandwidthMode property value. Specifies foreground and background bandwidth usage using percentages, absolutes, or hours.
        Args:
            value: Value to set for the bandwidthMode property.
        """
        self._bandwidth_mode = value
    
    @property
    def cache_server_background_download_fallback_to_http_delay_in_seconds(self,) -> Optional[int]:
        """
        Gets the cacheServerBackgroundDownloadFallbackToHttpDelayInSeconds property value. Specifies number of seconds to delay a fall back from cache servers to an HTTP source for a background download. Valid values 0 to 2592000.
        Returns: Optional[int]
        """
        return self._cache_server_background_download_fallback_to_http_delay_in_seconds
    
    @cache_server_background_download_fallback_to_http_delay_in_seconds.setter
    def cache_server_background_download_fallback_to_http_delay_in_seconds(self,value: Optional[int] = None) -> None:
        """
        Sets the cacheServerBackgroundDownloadFallbackToHttpDelayInSeconds property value. Specifies number of seconds to delay a fall back from cache servers to an HTTP source for a background download. Valid values 0 to 2592000.
        Args:
            value: Value to set for the cacheServerBackgroundDownloadFallbackToHttpDelayInSeconds property.
        """
        self._cache_server_background_download_fallback_to_http_delay_in_seconds = value
    
    @property
    def cache_server_foreground_download_fallback_to_http_delay_in_seconds(self,) -> Optional[int]:
        """
        Gets the cacheServerForegroundDownloadFallbackToHttpDelayInSeconds property value. Specifies number of seconds to delay a fall back from cache servers to an HTTP source for a foreground download. Valid values 0 to 2592000.​
        Returns: Optional[int]
        """
        return self._cache_server_foreground_download_fallback_to_http_delay_in_seconds
    
    @cache_server_foreground_download_fallback_to_http_delay_in_seconds.setter
    def cache_server_foreground_download_fallback_to_http_delay_in_seconds(self,value: Optional[int] = None) -> None:
        """
        Sets the cacheServerForegroundDownloadFallbackToHttpDelayInSeconds property value. Specifies number of seconds to delay a fall back from cache servers to an HTTP source for a foreground download. Valid values 0 to 2592000.​
        Args:
            value: Value to set for the cacheServerForegroundDownloadFallbackToHttpDelayInSeconds property.
        """
        self._cache_server_foreground_download_fallback_to_http_delay_in_seconds = value
    
    @property
    def cache_server_host_names(self,) -> Optional[List[str]]:
        """
        Gets the cacheServerHostNames property value. Specifies cache servers host names.
        Returns: Optional[List[str]]
        """
        return self._cache_server_host_names
    
    @cache_server_host_names.setter
    def cache_server_host_names(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the cacheServerHostNames property value. Specifies cache servers host names.
        Args:
            value: Value to set for the cacheServerHostNames property.
        """
        self._cache_server_host_names = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsDeliveryOptimizationConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsDeliveryOptimizationConfiguration"
        # Specifies number of seconds to delay an HTTP source in a background download that is allowed to use peer-to-peer. Valid values 0 to 4294967295
        self._background_download_from_http_delay_in_seconds: Optional[int] = None
        # Specifies foreground and background bandwidth usage using percentages, absolutes, or hours.
        self._bandwidth_mode: Optional[delivery_optimization_bandwidth.DeliveryOptimizationBandwidth] = None
        # Specifies number of seconds to delay a fall back from cache servers to an HTTP source for a background download. Valid values 0 to 2592000.
        self._cache_server_background_download_fallback_to_http_delay_in_seconds: Optional[int] = None
        # Specifies number of seconds to delay a fall back from cache servers to an HTTP source for a foreground download. Valid values 0 to 2592000.​
        self._cache_server_foreground_download_fallback_to_http_delay_in_seconds: Optional[int] = None
        # Specifies cache servers host names.
        self._cache_server_host_names: Optional[List[str]] = None
        # Delivery optimization mode for peer distribution
        self._delivery_optimization_mode: Optional[windows_delivery_optimization_mode.WindowsDeliveryOptimizationMode] = None
        # Specifies number of seconds to delay an HTTP source in a foreground download that is allowed to use peer-to-peer (0-86400). Valid values 0 to 86400
        self._foreground_download_from_http_delay_in_seconds: Optional[int] = None
        # Specifies to restrict peer selection to a specfic source.
        self._group_id_source: Optional[delivery_optimization_group_id_source.DeliveryOptimizationGroupIdSource] = None
        # Specifies the maximum time in days that each file is held in the Delivery Optimization cache after downloading successfully (0-3650). Valid values 0 to 3650
        self._maximum_cache_age_in_days: Optional[int] = None
        # Specifies the maximum cache size that Delivery Optimization either as a percentage or in GB.
        self._maximum_cache_size: Optional[delivery_optimization_max_cache_size.DeliveryOptimizationMaxCacheSize] = None
        # Specifies the minimum battery percentage to allow the device to upload data (0-100). Valid values 0 to 100
        self._minimum_battery_percentage_allowed_to_upload: Optional[int] = None
        # Specifies the minimum disk size in GB to use Peer Caching (1-100000). Valid values 1 to 100000
        self._minimum_disk_size_allowed_to_peer_in_gigabytes: Optional[int] = None
        # Specifies the minimum content file size in MB enabled to use Peer Caching (1-100000). Valid values 1 to 100000
        self._minimum_file_size_to_cache_in_megabytes: Optional[int] = None
        # Specifies the minimum RAM size in GB to use Peer Caching (1-100000). Valid values 1 to 100000
        self._minimum_ram_allowed_to_peer_in_gigabytes: Optional[int] = None
        # Specifies the drive that Delivery Optimization should use for its cache.
        self._modify_cache_location: Optional[str] = None
        # Values to restrict peer selection by.
        self._restrict_peer_selection_by: Optional[delivery_optimization_restrict_peer_selection_by_options.DeliveryOptimizationRestrictPeerSelectionByOptions] = None
        # Possible values of a property
        self._vpn_peer_caching: Optional[enablement.Enablement] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsDeliveryOptimizationConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsDeliveryOptimizationConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsDeliveryOptimizationConfiguration()
    
    @property
    def delivery_optimization_mode(self,) -> Optional[windows_delivery_optimization_mode.WindowsDeliveryOptimizationMode]:
        """
        Gets the deliveryOptimizationMode property value. Delivery optimization mode for peer distribution
        Returns: Optional[windows_delivery_optimization_mode.WindowsDeliveryOptimizationMode]
        """
        return self._delivery_optimization_mode
    
    @delivery_optimization_mode.setter
    def delivery_optimization_mode(self,value: Optional[windows_delivery_optimization_mode.WindowsDeliveryOptimizationMode] = None) -> None:
        """
        Sets the deliveryOptimizationMode property value. Delivery optimization mode for peer distribution
        Args:
            value: Value to set for the deliveryOptimizationMode property.
        """
        self._delivery_optimization_mode = value
    
    @property
    def foreground_download_from_http_delay_in_seconds(self,) -> Optional[int]:
        """
        Gets the foregroundDownloadFromHttpDelayInSeconds property value. Specifies number of seconds to delay an HTTP source in a foreground download that is allowed to use peer-to-peer (0-86400). Valid values 0 to 86400
        Returns: Optional[int]
        """
        return self._foreground_download_from_http_delay_in_seconds
    
    @foreground_download_from_http_delay_in_seconds.setter
    def foreground_download_from_http_delay_in_seconds(self,value: Optional[int] = None) -> None:
        """
        Sets the foregroundDownloadFromHttpDelayInSeconds property value. Specifies number of seconds to delay an HTTP source in a foreground download that is allowed to use peer-to-peer (0-86400). Valid values 0 to 86400
        Args:
            value: Value to set for the foregroundDownloadFromHttpDelayInSeconds property.
        """
        self._foreground_download_from_http_delay_in_seconds = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "background_download_from_http_delay_in_seconds": lambda n : setattr(self, 'background_download_from_http_delay_in_seconds', n.get_int_value()),
            "bandwidth_mode": lambda n : setattr(self, 'bandwidth_mode', n.get_object_value(delivery_optimization_bandwidth.DeliveryOptimizationBandwidth)),
            "cache_server_background_download_fallback_to_http_delay_in_seconds": lambda n : setattr(self, 'cache_server_background_download_fallback_to_http_delay_in_seconds', n.get_int_value()),
            "cache_server_foreground_download_fallback_to_http_delay_in_seconds": lambda n : setattr(self, 'cache_server_foreground_download_fallback_to_http_delay_in_seconds', n.get_int_value()),
            "cache_server_host_names": lambda n : setattr(self, 'cache_server_host_names', n.get_collection_of_primitive_values(str)),
            "delivery_optimization_mode": lambda n : setattr(self, 'delivery_optimization_mode', n.get_enum_value(windows_delivery_optimization_mode.WindowsDeliveryOptimizationMode)),
            "foreground_download_from_http_delay_in_seconds": lambda n : setattr(self, 'foreground_download_from_http_delay_in_seconds', n.get_int_value()),
            "group_id_source": lambda n : setattr(self, 'group_id_source', n.get_object_value(delivery_optimization_group_id_source.DeliveryOptimizationGroupIdSource)),
            "maximum_cache_age_in_days": lambda n : setattr(self, 'maximum_cache_age_in_days', n.get_int_value()),
            "maximum_cache_size": lambda n : setattr(self, 'maximum_cache_size', n.get_object_value(delivery_optimization_max_cache_size.DeliveryOptimizationMaxCacheSize)),
            "minimum_battery_percentage_allowed_to_upload": lambda n : setattr(self, 'minimum_battery_percentage_allowed_to_upload', n.get_int_value()),
            "minimum_disk_size_allowed_to_peer_in_gigabytes": lambda n : setattr(self, 'minimum_disk_size_allowed_to_peer_in_gigabytes', n.get_int_value()),
            "minimum_file_size_to_cache_in_megabytes": lambda n : setattr(self, 'minimum_file_size_to_cache_in_megabytes', n.get_int_value()),
            "minimum_ram_allowed_to_peer_in_gigabytes": lambda n : setattr(self, 'minimum_ram_allowed_to_peer_in_gigabytes', n.get_int_value()),
            "modify_cache_location": lambda n : setattr(self, 'modify_cache_location', n.get_str_value()),
            "restrict_peer_selection_by": lambda n : setattr(self, 'restrict_peer_selection_by', n.get_enum_value(delivery_optimization_restrict_peer_selection_by_options.DeliveryOptimizationRestrictPeerSelectionByOptions)),
            "vpn_peer_caching": lambda n : setattr(self, 'vpn_peer_caching', n.get_enum_value(enablement.Enablement)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group_id_source(self,) -> Optional[delivery_optimization_group_id_source.DeliveryOptimizationGroupIdSource]:
        """
        Gets the groupIdSource property value. Specifies to restrict peer selection to a specfic source.
        Returns: Optional[delivery_optimization_group_id_source.DeliveryOptimizationGroupIdSource]
        """
        return self._group_id_source
    
    @group_id_source.setter
    def group_id_source(self,value: Optional[delivery_optimization_group_id_source.DeliveryOptimizationGroupIdSource] = None) -> None:
        """
        Sets the groupIdSource property value. Specifies to restrict peer selection to a specfic source.
        Args:
            value: Value to set for the groupIdSource property.
        """
        self._group_id_source = value
    
    @property
    def maximum_cache_age_in_days(self,) -> Optional[int]:
        """
        Gets the maximumCacheAgeInDays property value. Specifies the maximum time in days that each file is held in the Delivery Optimization cache after downloading successfully (0-3650). Valid values 0 to 3650
        Returns: Optional[int]
        """
        return self._maximum_cache_age_in_days
    
    @maximum_cache_age_in_days.setter
    def maximum_cache_age_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the maximumCacheAgeInDays property value. Specifies the maximum time in days that each file is held in the Delivery Optimization cache after downloading successfully (0-3650). Valid values 0 to 3650
        Args:
            value: Value to set for the maximumCacheAgeInDays property.
        """
        self._maximum_cache_age_in_days = value
    
    @property
    def maximum_cache_size(self,) -> Optional[delivery_optimization_max_cache_size.DeliveryOptimizationMaxCacheSize]:
        """
        Gets the maximumCacheSize property value. Specifies the maximum cache size that Delivery Optimization either as a percentage or in GB.
        Returns: Optional[delivery_optimization_max_cache_size.DeliveryOptimizationMaxCacheSize]
        """
        return self._maximum_cache_size
    
    @maximum_cache_size.setter
    def maximum_cache_size(self,value: Optional[delivery_optimization_max_cache_size.DeliveryOptimizationMaxCacheSize] = None) -> None:
        """
        Sets the maximumCacheSize property value. Specifies the maximum cache size that Delivery Optimization either as a percentage or in GB.
        Args:
            value: Value to set for the maximumCacheSize property.
        """
        self._maximum_cache_size = value
    
    @property
    def minimum_battery_percentage_allowed_to_upload(self,) -> Optional[int]:
        """
        Gets the minimumBatteryPercentageAllowedToUpload property value. Specifies the minimum battery percentage to allow the device to upload data (0-100). Valid values 0 to 100
        Returns: Optional[int]
        """
        return self._minimum_battery_percentage_allowed_to_upload
    
    @minimum_battery_percentage_allowed_to_upload.setter
    def minimum_battery_percentage_allowed_to_upload(self,value: Optional[int] = None) -> None:
        """
        Sets the minimumBatteryPercentageAllowedToUpload property value. Specifies the minimum battery percentage to allow the device to upload data (0-100). Valid values 0 to 100
        Args:
            value: Value to set for the minimumBatteryPercentageAllowedToUpload property.
        """
        self._minimum_battery_percentage_allowed_to_upload = value
    
    @property
    def minimum_disk_size_allowed_to_peer_in_gigabytes(self,) -> Optional[int]:
        """
        Gets the minimumDiskSizeAllowedToPeerInGigabytes property value. Specifies the minimum disk size in GB to use Peer Caching (1-100000). Valid values 1 to 100000
        Returns: Optional[int]
        """
        return self._minimum_disk_size_allowed_to_peer_in_gigabytes
    
    @minimum_disk_size_allowed_to_peer_in_gigabytes.setter
    def minimum_disk_size_allowed_to_peer_in_gigabytes(self,value: Optional[int] = None) -> None:
        """
        Sets the minimumDiskSizeAllowedToPeerInGigabytes property value. Specifies the minimum disk size in GB to use Peer Caching (1-100000). Valid values 1 to 100000
        Args:
            value: Value to set for the minimumDiskSizeAllowedToPeerInGigabytes property.
        """
        self._minimum_disk_size_allowed_to_peer_in_gigabytes = value
    
    @property
    def minimum_file_size_to_cache_in_megabytes(self,) -> Optional[int]:
        """
        Gets the minimumFileSizeToCacheInMegabytes property value. Specifies the minimum content file size in MB enabled to use Peer Caching (1-100000). Valid values 1 to 100000
        Returns: Optional[int]
        """
        return self._minimum_file_size_to_cache_in_megabytes
    
    @minimum_file_size_to_cache_in_megabytes.setter
    def minimum_file_size_to_cache_in_megabytes(self,value: Optional[int] = None) -> None:
        """
        Sets the minimumFileSizeToCacheInMegabytes property value. Specifies the minimum content file size in MB enabled to use Peer Caching (1-100000). Valid values 1 to 100000
        Args:
            value: Value to set for the minimumFileSizeToCacheInMegabytes property.
        """
        self._minimum_file_size_to_cache_in_megabytes = value
    
    @property
    def minimum_ram_allowed_to_peer_in_gigabytes(self,) -> Optional[int]:
        """
        Gets the minimumRamAllowedToPeerInGigabytes property value. Specifies the minimum RAM size in GB to use Peer Caching (1-100000). Valid values 1 to 100000
        Returns: Optional[int]
        """
        return self._minimum_ram_allowed_to_peer_in_gigabytes
    
    @minimum_ram_allowed_to_peer_in_gigabytes.setter
    def minimum_ram_allowed_to_peer_in_gigabytes(self,value: Optional[int] = None) -> None:
        """
        Sets the minimumRamAllowedToPeerInGigabytes property value. Specifies the minimum RAM size in GB to use Peer Caching (1-100000). Valid values 1 to 100000
        Args:
            value: Value to set for the minimumRamAllowedToPeerInGigabytes property.
        """
        self._minimum_ram_allowed_to_peer_in_gigabytes = value
    
    @property
    def modify_cache_location(self,) -> Optional[str]:
        """
        Gets the modifyCacheLocation property value. Specifies the drive that Delivery Optimization should use for its cache.
        Returns: Optional[str]
        """
        return self._modify_cache_location
    
    @modify_cache_location.setter
    def modify_cache_location(self,value: Optional[str] = None) -> None:
        """
        Sets the modifyCacheLocation property value. Specifies the drive that Delivery Optimization should use for its cache.
        Args:
            value: Value to set for the modifyCacheLocation property.
        """
        self._modify_cache_location = value
    
    @property
    def restrict_peer_selection_by(self,) -> Optional[delivery_optimization_restrict_peer_selection_by_options.DeliveryOptimizationRestrictPeerSelectionByOptions]:
        """
        Gets the restrictPeerSelectionBy property value. Values to restrict peer selection by.
        Returns: Optional[delivery_optimization_restrict_peer_selection_by_options.DeliveryOptimizationRestrictPeerSelectionByOptions]
        """
        return self._restrict_peer_selection_by
    
    @restrict_peer_selection_by.setter
    def restrict_peer_selection_by(self,value: Optional[delivery_optimization_restrict_peer_selection_by_options.DeliveryOptimizationRestrictPeerSelectionByOptions] = None) -> None:
        """
        Sets the restrictPeerSelectionBy property value. Values to restrict peer selection by.
        Args:
            value: Value to set for the restrictPeerSelectionBy property.
        """
        self._restrict_peer_selection_by = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("backgroundDownloadFromHttpDelayInSeconds", self.background_download_from_http_delay_in_seconds)
        writer.write_object_value("bandwidthMode", self.bandwidth_mode)
        writer.write_int_value("cacheServerBackgroundDownloadFallbackToHttpDelayInSeconds", self.cache_server_background_download_fallback_to_http_delay_in_seconds)
        writer.write_int_value("cacheServerForegroundDownloadFallbackToHttpDelayInSeconds", self.cache_server_foreground_download_fallback_to_http_delay_in_seconds)
        writer.write_collection_of_primitive_values("cacheServerHostNames", self.cache_server_host_names)
        writer.write_enum_value("deliveryOptimizationMode", self.delivery_optimization_mode)
        writer.write_int_value("foregroundDownloadFromHttpDelayInSeconds", self.foreground_download_from_http_delay_in_seconds)
        writer.write_object_value("groupIdSource", self.group_id_source)
        writer.write_int_value("maximumCacheAgeInDays", self.maximum_cache_age_in_days)
        writer.write_object_value("maximumCacheSize", self.maximum_cache_size)
        writer.write_int_value("minimumBatteryPercentageAllowedToUpload", self.minimum_battery_percentage_allowed_to_upload)
        writer.write_int_value("minimumDiskSizeAllowedToPeerInGigabytes", self.minimum_disk_size_allowed_to_peer_in_gigabytes)
        writer.write_int_value("minimumFileSizeToCacheInMegabytes", self.minimum_file_size_to_cache_in_megabytes)
        writer.write_int_value("minimumRamAllowedToPeerInGigabytes", self.minimum_ram_allowed_to_peer_in_gigabytes)
        writer.write_str_value("modifyCacheLocation", self.modify_cache_location)
        writer.write_enum_value("restrictPeerSelectionBy", self.restrict_peer_selection_by)
        writer.write_enum_value("vpnPeerCaching", self.vpn_peer_caching)
    
    @property
    def vpn_peer_caching(self,) -> Optional[enablement.Enablement]:
        """
        Gets the vpnPeerCaching property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._vpn_peer_caching
    
    @vpn_peer_caching.setter
    def vpn_peer_caching(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the vpnPeerCaching property value. Possible values of a property
        Args:
            value: Value to set for the vpnPeerCaching property.
        """
        self._vpn_peer_caching = value
    

