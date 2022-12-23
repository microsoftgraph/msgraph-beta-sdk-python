from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
logon_user = lazy_import('msgraph.generated.models.logon_user')
network_interface = lazy_import('msgraph.generated.models.network_interface')
security_vendor_information = lazy_import('msgraph.generated.models.security_vendor_information')

class HostSecurityProfile(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def azure_subscription_id(self,) -> Optional[str]:
        """
        Gets the azureSubscriptionId property value. The azureSubscriptionId property
        Returns: Optional[str]
        """
        return self._azure_subscription_id
    
    @azure_subscription_id.setter
    def azure_subscription_id(self,value: Optional[str] = None) -> None:
        """
        Sets the azureSubscriptionId property value. The azureSubscriptionId property
        Args:
            value: Value to set for the azureSubscriptionId property.
        """
        self._azure_subscription_id = value
    
    @property
    def azure_tenant_id(self,) -> Optional[str]:
        """
        Gets the azureTenantId property value. The azureTenantId property
        Returns: Optional[str]
        """
        return self._azure_tenant_id
    
    @azure_tenant_id.setter
    def azure_tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the azureTenantId property value. The azureTenantId property
        Args:
            value: Value to set for the azureTenantId property.
        """
        self._azure_tenant_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new hostSecurityProfile and sets the default values.
        """
        super().__init__()
        # The azureSubscriptionId property
        self._azure_subscription_id: Optional[str] = None
        # The azureTenantId property
        self._azure_tenant_id: Optional[str] = None
        # The firstSeenDateTime property
        self._first_seen_date_time: Optional[datetime] = None
        # The fqdn property
        self._fqdn: Optional[str] = None
        # The isAzureAdJoined property
        self._is_azure_ad_joined: Optional[bool] = None
        # The isAzureAdRegistered property
        self._is_azure_ad_registered: Optional[bool] = None
        # The isHybridAzureDomainJoined property
        self._is_hybrid_azure_domain_joined: Optional[bool] = None
        # The lastSeenDateTime property
        self._last_seen_date_time: Optional[datetime] = None
        # The logonUsers property
        self._logon_users: Optional[List[logon_user.LogonUser]] = None
        # The netBiosName property
        self._net_bios_name: Optional[str] = None
        # The networkInterfaces property
        self._network_interfaces: Optional[List[network_interface.NetworkInterface]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The os property
        self._os: Optional[str] = None
        # The osVersion property
        self._os_version: Optional[str] = None
        # The parentHost property
        self._parent_host: Optional[str] = None
        # The relatedHostIds property
        self._related_host_ids: Optional[List[str]] = None
        # The riskScore property
        self._risk_score: Optional[str] = None
        # The tags property
        self._tags: Optional[List[str]] = None
        # The vendorInformation property
        self._vendor_information: Optional[security_vendor_information.SecurityVendorInformation] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> HostSecurityProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: HostSecurityProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return HostSecurityProfile()
    
    @property
    def first_seen_date_time(self,) -> Optional[datetime]:
        """
        Gets the firstSeenDateTime property value. The firstSeenDateTime property
        Returns: Optional[datetime]
        """
        return self._first_seen_date_time
    
    @first_seen_date_time.setter
    def first_seen_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the firstSeenDateTime property value. The firstSeenDateTime property
        Args:
            value: Value to set for the firstSeenDateTime property.
        """
        self._first_seen_date_time = value
    
    @property
    def fqdn(self,) -> Optional[str]:
        """
        Gets the fqdn property value. The fqdn property
        Returns: Optional[str]
        """
        return self._fqdn
    
    @fqdn.setter
    def fqdn(self,value: Optional[str] = None) -> None:
        """
        Sets the fqdn property value. The fqdn property
        Args:
            value: Value to set for the fqdn property.
        """
        self._fqdn = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "azure_subscription_id": lambda n : setattr(self, 'azure_subscription_id', n.get_str_value()),
            "azure_tenant_id": lambda n : setattr(self, 'azure_tenant_id', n.get_str_value()),
            "first_seen_date_time": lambda n : setattr(self, 'first_seen_date_time', n.get_datetime_value()),
            "fqdn": lambda n : setattr(self, 'fqdn', n.get_str_value()),
            "is_azure_ad_joined": lambda n : setattr(self, 'is_azure_ad_joined', n.get_bool_value()),
            "is_azure_ad_registered": lambda n : setattr(self, 'is_azure_ad_registered', n.get_bool_value()),
            "is_hybrid_azure_domain_joined": lambda n : setattr(self, 'is_hybrid_azure_domain_joined', n.get_bool_value()),
            "last_seen_date_time": lambda n : setattr(self, 'last_seen_date_time', n.get_datetime_value()),
            "logon_users": lambda n : setattr(self, 'logon_users', n.get_collection_of_object_values(logon_user.LogonUser)),
            "net_bios_name": lambda n : setattr(self, 'net_bios_name', n.get_str_value()),
            "network_interfaces": lambda n : setattr(self, 'network_interfaces', n.get_collection_of_object_values(network_interface.NetworkInterface)),
            "os": lambda n : setattr(self, 'os', n.get_str_value()),
            "os_version": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "parent_host": lambda n : setattr(self, 'parent_host', n.get_str_value()),
            "related_host_ids": lambda n : setattr(self, 'related_host_ids', n.get_collection_of_primitive_values(str)),
            "risk_score": lambda n : setattr(self, 'risk_score', n.get_str_value()),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
            "vendor_information": lambda n : setattr(self, 'vendor_information', n.get_object_value(security_vendor_information.SecurityVendorInformation)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_azure_ad_joined(self,) -> Optional[bool]:
        """
        Gets the isAzureAdJoined property value. The isAzureAdJoined property
        Returns: Optional[bool]
        """
        return self._is_azure_ad_joined
    
    @is_azure_ad_joined.setter
    def is_azure_ad_joined(self,value: Optional[bool] = None) -> None:
        """
        Sets the isAzureAdJoined property value. The isAzureAdJoined property
        Args:
            value: Value to set for the isAzureAdJoined property.
        """
        self._is_azure_ad_joined = value
    
    @property
    def is_azure_ad_registered(self,) -> Optional[bool]:
        """
        Gets the isAzureAdRegistered property value. The isAzureAdRegistered property
        Returns: Optional[bool]
        """
        return self._is_azure_ad_registered
    
    @is_azure_ad_registered.setter
    def is_azure_ad_registered(self,value: Optional[bool] = None) -> None:
        """
        Sets the isAzureAdRegistered property value. The isAzureAdRegistered property
        Args:
            value: Value to set for the isAzureAdRegistered property.
        """
        self._is_azure_ad_registered = value
    
    @property
    def is_hybrid_azure_domain_joined(self,) -> Optional[bool]:
        """
        Gets the isHybridAzureDomainJoined property value. The isHybridAzureDomainJoined property
        Returns: Optional[bool]
        """
        return self._is_hybrid_azure_domain_joined
    
    @is_hybrid_azure_domain_joined.setter
    def is_hybrid_azure_domain_joined(self,value: Optional[bool] = None) -> None:
        """
        Sets the isHybridAzureDomainJoined property value. The isHybridAzureDomainJoined property
        Args:
            value: Value to set for the isHybridAzureDomainJoined property.
        """
        self._is_hybrid_azure_domain_joined = value
    
    @property
    def last_seen_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastSeenDateTime property value. The lastSeenDateTime property
        Returns: Optional[datetime]
        """
        return self._last_seen_date_time
    
    @last_seen_date_time.setter
    def last_seen_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastSeenDateTime property value. The lastSeenDateTime property
        Args:
            value: Value to set for the lastSeenDateTime property.
        """
        self._last_seen_date_time = value
    
    @property
    def logon_users(self,) -> Optional[List[logon_user.LogonUser]]:
        """
        Gets the logonUsers property value. The logonUsers property
        Returns: Optional[List[logon_user.LogonUser]]
        """
        return self._logon_users
    
    @logon_users.setter
    def logon_users(self,value: Optional[List[logon_user.LogonUser]] = None) -> None:
        """
        Sets the logonUsers property value. The logonUsers property
        Args:
            value: Value to set for the logonUsers property.
        """
        self._logon_users = value
    
    @property
    def net_bios_name(self,) -> Optional[str]:
        """
        Gets the netBiosName property value. The netBiosName property
        Returns: Optional[str]
        """
        return self._net_bios_name
    
    @net_bios_name.setter
    def net_bios_name(self,value: Optional[str] = None) -> None:
        """
        Sets the netBiosName property value. The netBiosName property
        Args:
            value: Value to set for the netBiosName property.
        """
        self._net_bios_name = value
    
    @property
    def network_interfaces(self,) -> Optional[List[network_interface.NetworkInterface]]:
        """
        Gets the networkInterfaces property value. The networkInterfaces property
        Returns: Optional[List[network_interface.NetworkInterface]]
        """
        return self._network_interfaces
    
    @network_interfaces.setter
    def network_interfaces(self,value: Optional[List[network_interface.NetworkInterface]] = None) -> None:
        """
        Sets the networkInterfaces property value. The networkInterfaces property
        Args:
            value: Value to set for the networkInterfaces property.
        """
        self._network_interfaces = value
    
    @property
    def os(self,) -> Optional[str]:
        """
        Gets the os property value. The os property
        Returns: Optional[str]
        """
        return self._os
    
    @os.setter
    def os(self,value: Optional[str] = None) -> None:
        """
        Sets the os property value. The os property
        Args:
            value: Value to set for the os property.
        """
        self._os = value
    
    @property
    def os_version(self,) -> Optional[str]:
        """
        Gets the osVersion property value. The osVersion property
        Returns: Optional[str]
        """
        return self._os_version
    
    @os_version.setter
    def os_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osVersion property value. The osVersion property
        Args:
            value: Value to set for the osVersion property.
        """
        self._os_version = value
    
    @property
    def parent_host(self,) -> Optional[str]:
        """
        Gets the parentHost property value. The parentHost property
        Returns: Optional[str]
        """
        return self._parent_host
    
    @parent_host.setter
    def parent_host(self,value: Optional[str] = None) -> None:
        """
        Sets the parentHost property value. The parentHost property
        Args:
            value: Value to set for the parentHost property.
        """
        self._parent_host = value
    
    @property
    def related_host_ids(self,) -> Optional[List[str]]:
        """
        Gets the relatedHostIds property value. The relatedHostIds property
        Returns: Optional[List[str]]
        """
        return self._related_host_ids
    
    @related_host_ids.setter
    def related_host_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the relatedHostIds property value. The relatedHostIds property
        Args:
            value: Value to set for the relatedHostIds property.
        """
        self._related_host_ids = value
    
    @property
    def risk_score(self,) -> Optional[str]:
        """
        Gets the riskScore property value. The riskScore property
        Returns: Optional[str]
        """
        return self._risk_score
    
    @risk_score.setter
    def risk_score(self,value: Optional[str] = None) -> None:
        """
        Sets the riskScore property value. The riskScore property
        Args:
            value: Value to set for the riskScore property.
        """
        self._risk_score = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("azureSubscriptionId", self.azure_subscription_id)
        writer.write_str_value("azureTenantId", self.azure_tenant_id)
        writer.write_datetime_value("firstSeenDateTime", self.first_seen_date_time)
        writer.write_str_value("fqdn", self.fqdn)
        writer.write_bool_value("isAzureAdJoined", self.is_azure_ad_joined)
        writer.write_bool_value("isAzureAdRegistered", self.is_azure_ad_registered)
        writer.write_bool_value("isHybridAzureDomainJoined", self.is_hybrid_azure_domain_joined)
        writer.write_datetime_value("lastSeenDateTime", self.last_seen_date_time)
        writer.write_collection_of_object_values("logonUsers", self.logon_users)
        writer.write_str_value("netBiosName", self.net_bios_name)
        writer.write_collection_of_object_values("networkInterfaces", self.network_interfaces)
        writer.write_str_value("os", self.os)
        writer.write_str_value("osVersion", self.os_version)
        writer.write_str_value("parentHost", self.parent_host)
        writer.write_collection_of_primitive_values("relatedHostIds", self.related_host_ids)
        writer.write_str_value("riskScore", self.risk_score)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_object_value("vendorInformation", self.vendor_information)
    
    @property
    def tags(self,) -> Optional[List[str]]:
        """
        Gets the tags property value. The tags property
        Returns: Optional[List[str]]
        """
        return self._tags
    
    @tags.setter
    def tags(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the tags property value. The tags property
        Args:
            value: Value to set for the tags property.
        """
        self._tags = value
    
    @property
    def vendor_information(self,) -> Optional[security_vendor_information.SecurityVendorInformation]:
        """
        Gets the vendorInformation property value. The vendorInformation property
        Returns: Optional[security_vendor_information.SecurityVendorInformation]
        """
        return self._vendor_information
    
    @vendor_information.setter
    def vendor_information(self,value: Optional[security_vendor_information.SecurityVendorInformation] = None) -> None:
        """
        Sets the vendorInformation property value. The vendorInformation property
        Args:
            value: Value to set for the vendorInformation property.
        """
        self._vendor_information = value
    

