from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

cloud_pc_management_service = lazy_import('msgraph.generated.models.cloud_pc_management_service')
cloud_pc_on_premises_connection_status = lazy_import('msgraph.generated.models.cloud_pc_on_premises_connection_status')
cloud_pc_on_premises_connection_status_details = lazy_import('msgraph.generated.models.cloud_pc_on_premises_connection_status_details')
cloud_pc_on_premises_connection_type = lazy_import('msgraph.generated.models.cloud_pc_on_premises_connection_type')
entity = lazy_import('msgraph.generated.models.entity')

class CloudPcOnPremisesConnection(entity.Entity):
    @property
    def ad_domain_name(self,) -> Optional[str]:
        """
        Gets the adDomainName property value. The fully qualified domain name (FQDN) of the Active Directory domain you want to join. Optional.
        Returns: Optional[str]
        """
        return self._ad_domain_name
    
    @ad_domain_name.setter
    def ad_domain_name(self,value: Optional[str] = None) -> None:
        """
        Sets the adDomainName property value. The fully qualified domain name (FQDN) of the Active Directory domain you want to join. Optional.
        Args:
            value: Value to set for the adDomainName property.
        """
        self._ad_domain_name = value
    
    @property
    def ad_domain_password(self,) -> Optional[str]:
        """
        Gets the adDomainPassword property value. The password associated with adDomainUsername.
        Returns: Optional[str]
        """
        return self._ad_domain_password
    
    @ad_domain_password.setter
    def ad_domain_password(self,value: Optional[str] = None) -> None:
        """
        Sets the adDomainPassword property value. The password associated with adDomainUsername.
        Args:
            value: Value to set for the adDomainPassword property.
        """
        self._ad_domain_password = value
    
    @property
    def ad_domain_username(self,) -> Optional[str]:
        """
        Gets the adDomainUsername property value. The username of an Active Directory account (user or service account) that has permissions to create computer objects in Active Directory. Required format: admin@contoso.com. Optional.
        Returns: Optional[str]
        """
        return self._ad_domain_username
    
    @ad_domain_username.setter
    def ad_domain_username(self,value: Optional[str] = None) -> None:
        """
        Sets the adDomainUsername property value. The username of an Active Directory account (user or service account) that has permissions to create computer objects in Active Directory. Required format: admin@contoso.com. Optional.
        Args:
            value: Value to set for the adDomainUsername property.
        """
        self._ad_domain_username = value
    
    @property
    def alternate_resource_url(self,) -> Optional[str]:
        """
        Gets the alternateResourceUrl property value. The interface URL of the partner service's resource that links to this Azure network connection. Returned only on $select.
        Returns: Optional[str]
        """
        return self._alternate_resource_url
    
    @alternate_resource_url.setter
    def alternate_resource_url(self,value: Optional[str] = None) -> None:
        """
        Sets the alternateResourceUrl property value. The interface URL of the partner service's resource that links to this Azure network connection. Returned only on $select.
        Args:
            value: Value to set for the alternateResourceUrl property.
        """
        self._alternate_resource_url = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new CloudPcOnPremisesConnection and sets the default values.
        """
        super().__init__()
        # The fully qualified domain name (FQDN) of the Active Directory domain you want to join. Optional.
        self._ad_domain_name: Optional[str] = None
        # The password associated with adDomainUsername.
        self._ad_domain_password: Optional[str] = None
        # The username of an Active Directory account (user or service account) that has permissions to create computer objects in Active Directory. Required format: admin@contoso.com. Optional.
        self._ad_domain_username: Optional[str] = None
        # The interface URL of the partner service's resource that links to this Azure network connection. Returned only on $select.
        self._alternate_resource_url: Optional[str] = None
        # The display name for the Azure network connection.
        self._display_name: Optional[str] = None
        # The healthCheckStatus property
        self._health_check_status: Optional[cloud_pc_on_premises_connection_status.CloudPcOnPremisesConnectionStatus] = None
        # The details of the connection's health checks and the corresponding results. Returned only on $select. For an example that shows how to get the inUse property, see Example 2: Get the selected properties of an Azure network connection, including healthCheckStatusDetails. Read-only.
        self._health_check_status_details: Optional[cloud_pc_on_premises_connection_status_details.CloudPcOnPremisesConnectionStatusDetails] = None
        # When true, the Azure network connection is in use. When false, the connection is not in use. You cannot delete a connection that’s in use. Returned only on $select. For an example that shows how to get the inUse property, see Example 2: Get the selected properties of an Azure network connection, including healthCheckStatusDetails. Read-only.
        self._in_use: Optional[bool] = None
        # The managedBy property
        self._managed_by: Optional[cloud_pc_management_service.CloudPcManagementService] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The organizational unit (OU) in which the computer account is created. If left null, the OU that’s configured as the default (a well-known computer object container) in your Active Directory domain (OU) is used. Optional.
        self._organizational_unit: Optional[str] = None
        # The ID of the target resource group. Required format: /subscriptions/{subscription-id}/resourceGroups/{resourceGroupName}.
        self._resource_group_id: Optional[str] = None
        # The ID of the target subnet. Required format: /subscriptions/{subscription-id}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkId}/subnets/{subnetName}.
        self._subnet_id: Optional[str] = None
        # The ID of the target Azure subscription that’s associated with your tenant.
        self._subscription_id: Optional[str] = None
        # The name of the target Azure subscription. Read-only.
        self._subscription_name: Optional[str] = None
        # Specifies how the provisioned Cloud PC will be joined to Azure Active Directory. Default value is hybridAzureADJoin. Possible values are: azureADJoin, hybridAzureADJoin, unknownFutureValue.
        self._type: Optional[cloud_pc_on_premises_connection_type.CloudPcOnPremisesConnectionType] = None
        # The ID of the target virtual network. Required format: /subscriptions/{subscription-id}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}.
        self._virtual_network_id: Optional[str] = None
        # The virtualNetworkLocation property
        self._virtual_network_location: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcOnPremisesConnection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcOnPremisesConnection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcOnPremisesConnection()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name for the Azure network connection.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for the Azure network connection.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "ad_domain_name": lambda n : setattr(self, 'ad_domain_name', n.get_str_value()),
            "ad_domain_password": lambda n : setattr(self, 'ad_domain_password', n.get_str_value()),
            "ad_domain_username": lambda n : setattr(self, 'ad_domain_username', n.get_str_value()),
            "alternate_resource_url": lambda n : setattr(self, 'alternate_resource_url', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "health_check_status": lambda n : setattr(self, 'health_check_status', n.get_enum_value(cloud_pc_on_premises_connection_status.CloudPcOnPremisesConnectionStatus)),
            "health_check_status_details": lambda n : setattr(self, 'health_check_status_details', n.get_object_value(cloud_pc_on_premises_connection_status_details.CloudPcOnPremisesConnectionStatusDetails)),
            "in_use": lambda n : setattr(self, 'in_use', n.get_bool_value()),
            "managed_by": lambda n : setattr(self, 'managed_by', n.get_enum_value(cloud_pc_management_service.CloudPcManagementService)),
            "organizational_unit": lambda n : setattr(self, 'organizational_unit', n.get_str_value()),
            "resource_group_id": lambda n : setattr(self, 'resource_group_id', n.get_str_value()),
            "subnet_id": lambda n : setattr(self, 'subnet_id', n.get_str_value()),
            "subscription_id": lambda n : setattr(self, 'subscription_id', n.get_str_value()),
            "subscription_name": lambda n : setattr(self, 'subscription_name', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(cloud_pc_on_premises_connection_type.CloudPcOnPremisesConnectionType)),
            "virtual_network_id": lambda n : setattr(self, 'virtual_network_id', n.get_str_value()),
            "virtual_network_location": lambda n : setattr(self, 'virtual_network_location', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def health_check_status(self,) -> Optional[cloud_pc_on_premises_connection_status.CloudPcOnPremisesConnectionStatus]:
        """
        Gets the healthCheckStatus property value. The healthCheckStatus property
        Returns: Optional[cloud_pc_on_premises_connection_status.CloudPcOnPremisesConnectionStatus]
        """
        return self._health_check_status
    
    @health_check_status.setter
    def health_check_status(self,value: Optional[cloud_pc_on_premises_connection_status.CloudPcOnPremisesConnectionStatus] = None) -> None:
        """
        Sets the healthCheckStatus property value. The healthCheckStatus property
        Args:
            value: Value to set for the healthCheckStatus property.
        """
        self._health_check_status = value
    
    @property
    def health_check_status_details(self,) -> Optional[cloud_pc_on_premises_connection_status_details.CloudPcOnPremisesConnectionStatusDetails]:
        """
        Gets the healthCheckStatusDetails property value. The details of the connection's health checks and the corresponding results. Returned only on $select. For an example that shows how to get the inUse property, see Example 2: Get the selected properties of an Azure network connection, including healthCheckStatusDetails. Read-only.
        Returns: Optional[cloud_pc_on_premises_connection_status_details.CloudPcOnPremisesConnectionStatusDetails]
        """
        return self._health_check_status_details
    
    @health_check_status_details.setter
    def health_check_status_details(self,value: Optional[cloud_pc_on_premises_connection_status_details.CloudPcOnPremisesConnectionStatusDetails] = None) -> None:
        """
        Sets the healthCheckStatusDetails property value. The details of the connection's health checks and the corresponding results. Returned only on $select. For an example that shows how to get the inUse property, see Example 2: Get the selected properties of an Azure network connection, including healthCheckStatusDetails. Read-only.
        Args:
            value: Value to set for the healthCheckStatusDetails property.
        """
        self._health_check_status_details = value
    
    @property
    def in_use(self,) -> Optional[bool]:
        """
        Gets the inUse property value. When true, the Azure network connection is in use. When false, the connection is not in use. You cannot delete a connection that’s in use. Returned only on $select. For an example that shows how to get the inUse property, see Example 2: Get the selected properties of an Azure network connection, including healthCheckStatusDetails. Read-only.
        Returns: Optional[bool]
        """
        return self._in_use
    
    @in_use.setter
    def in_use(self,value: Optional[bool] = None) -> None:
        """
        Sets the inUse property value. When true, the Azure network connection is in use. When false, the connection is not in use. You cannot delete a connection that’s in use. Returned only on $select. For an example that shows how to get the inUse property, see Example 2: Get the selected properties of an Azure network connection, including healthCheckStatusDetails. Read-only.
        Args:
            value: Value to set for the inUse property.
        """
        self._in_use = value
    
    @property
    def managed_by(self,) -> Optional[cloud_pc_management_service.CloudPcManagementService]:
        """
        Gets the managedBy property value. The managedBy property
        Returns: Optional[cloud_pc_management_service.CloudPcManagementService]
        """
        return self._managed_by
    
    @managed_by.setter
    def managed_by(self,value: Optional[cloud_pc_management_service.CloudPcManagementService] = None) -> None:
        """
        Sets the managedBy property value. The managedBy property
        Args:
            value: Value to set for the managedBy property.
        """
        self._managed_by = value
    
    @property
    def organizational_unit(self,) -> Optional[str]:
        """
        Gets the organizationalUnit property value. The organizational unit (OU) in which the computer account is created. If left null, the OU that’s configured as the default (a well-known computer object container) in your Active Directory domain (OU) is used. Optional.
        Returns: Optional[str]
        """
        return self._organizational_unit
    
    @organizational_unit.setter
    def organizational_unit(self,value: Optional[str] = None) -> None:
        """
        Sets the organizationalUnit property value. The organizational unit (OU) in which the computer account is created. If left null, the OU that’s configured as the default (a well-known computer object container) in your Active Directory domain (OU) is used. Optional.
        Args:
            value: Value to set for the organizationalUnit property.
        """
        self._organizational_unit = value
    
    @property
    def resource_group_id(self,) -> Optional[str]:
        """
        Gets the resourceGroupId property value. The ID of the target resource group. Required format: /subscriptions/{subscription-id}/resourceGroups/{resourceGroupName}.
        Returns: Optional[str]
        """
        return self._resource_group_id
    
    @resource_group_id.setter
    def resource_group_id(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceGroupId property value. The ID of the target resource group. Required format: /subscriptions/{subscription-id}/resourceGroups/{resourceGroupName}.
        Args:
            value: Value to set for the resourceGroupId property.
        """
        self._resource_group_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("adDomainName", self.ad_domain_name)
        writer.write_str_value("adDomainPassword", self.ad_domain_password)
        writer.write_str_value("adDomainUsername", self.ad_domain_username)
        writer.write_str_value("alternateResourceUrl", self.alternate_resource_url)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("healthCheckStatus", self.health_check_status)
        writer.write_object_value("healthCheckStatusDetails", self.health_check_status_details)
        writer.write_bool_value("inUse", self.in_use)
        writer.write_enum_value("managedBy", self.managed_by)
        writer.write_str_value("organizationalUnit", self.organizational_unit)
        writer.write_str_value("resourceGroupId", self.resource_group_id)
        writer.write_str_value("subnetId", self.subnet_id)
        writer.write_str_value("subscriptionId", self.subscription_id)
        writer.write_str_value("subscriptionName", self.subscription_name)
        writer.write_enum_value("type", self.type)
        writer.write_str_value("virtualNetworkId", self.virtual_network_id)
        writer.write_str_value("virtualNetworkLocation", self.virtual_network_location)
    
    @property
    def subnet_id(self,) -> Optional[str]:
        """
        Gets the subnetId property value. The ID of the target subnet. Required format: /subscriptions/{subscription-id}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkId}/subnets/{subnetName}.
        Returns: Optional[str]
        """
        return self._subnet_id
    
    @subnet_id.setter
    def subnet_id(self,value: Optional[str] = None) -> None:
        """
        Sets the subnetId property value. The ID of the target subnet. Required format: /subscriptions/{subscription-id}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkId}/subnets/{subnetName}.
        Args:
            value: Value to set for the subnetId property.
        """
        self._subnet_id = value
    
    @property
    def subscription_id(self,) -> Optional[str]:
        """
        Gets the subscriptionId property value. The ID of the target Azure subscription that’s associated with your tenant.
        Returns: Optional[str]
        """
        return self._subscription_id
    
    @subscription_id.setter
    def subscription_id(self,value: Optional[str] = None) -> None:
        """
        Sets the subscriptionId property value. The ID of the target Azure subscription that’s associated with your tenant.
        Args:
            value: Value to set for the subscriptionId property.
        """
        self._subscription_id = value
    
    @property
    def subscription_name(self,) -> Optional[str]:
        """
        Gets the subscriptionName property value. The name of the target Azure subscription. Read-only.
        Returns: Optional[str]
        """
        return self._subscription_name
    
    @subscription_name.setter
    def subscription_name(self,value: Optional[str] = None) -> None:
        """
        Sets the subscriptionName property value. The name of the target Azure subscription. Read-only.
        Args:
            value: Value to set for the subscriptionName property.
        """
        self._subscription_name = value
    
    @property
    def type(self,) -> Optional[cloud_pc_on_premises_connection_type.CloudPcOnPremisesConnectionType]:
        """
        Gets the type property value. Specifies how the provisioned Cloud PC will be joined to Azure Active Directory. Default value is hybridAzureADJoin. Possible values are: azureADJoin, hybridAzureADJoin, unknownFutureValue.
        Returns: Optional[cloud_pc_on_premises_connection_type.CloudPcOnPremisesConnectionType]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[cloud_pc_on_premises_connection_type.CloudPcOnPremisesConnectionType] = None) -> None:
        """
        Sets the type property value. Specifies how the provisioned Cloud PC will be joined to Azure Active Directory. Default value is hybridAzureADJoin. Possible values are: azureADJoin, hybridAzureADJoin, unknownFutureValue.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    
    @property
    def virtual_network_id(self,) -> Optional[str]:
        """
        Gets the virtualNetworkId property value. The ID of the target virtual network. Required format: /subscriptions/{subscription-id}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}.
        Returns: Optional[str]
        """
        return self._virtual_network_id
    
    @virtual_network_id.setter
    def virtual_network_id(self,value: Optional[str] = None) -> None:
        """
        Sets the virtualNetworkId property value. The ID of the target virtual network. Required format: /subscriptions/{subscription-id}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}.
        Args:
            value: Value to set for the virtualNetworkId property.
        """
        self._virtual_network_id = value
    
    @property
    def virtual_network_location(self,) -> Optional[str]:
        """
        Gets the virtualNetworkLocation property value. The virtualNetworkLocation property
        Returns: Optional[str]
        """
        return self._virtual_network_location
    
    @virtual_network_location.setter
    def virtual_network_location(self,value: Optional[str] = None) -> None:
        """
        Sets the virtualNetworkLocation property value. The virtualNetworkLocation property
        Args:
            value: Value to set for the virtualNetworkLocation property.
        """
        self._virtual_network_location = value
    

