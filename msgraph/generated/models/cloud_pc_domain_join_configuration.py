from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

cloud_pc_domain_join_type = lazy_import('msgraph.generated.models.cloud_pc_domain_join_type')
cloud_pc_region_group = lazy_import('msgraph.generated.models.cloud_pc_region_group')

class CloudPcDomainJoinConfiguration(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new cloudPcDomainJoinConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The Azure network connection ID that matches the virtual network IT admins want the provisioning policy to use when they create Cloud PCs. You can use this property in both domain join types: Azure AD joined or Hybrid Azure AD joined. If you enter an onPremisesConnectionId, leave regionName as empty.
        self._on_premises_connection_id: Optional[str] = None
        # The regionGroup property
        self._region_group: Optional[cloud_pc_region_group.CloudPcRegionGroup] = None
        # The supported Azure region where the IT admin wants the provisioning policy to create Cloud PCs. The underlying virtual network will be created and managed by the Windows 365 service. This can only be entered if the IT admin chooses Azure AD joined as the domain join type. If you enter a regionName, leave onPremisesConnectionId as empty.
        self._region_name: Optional[str] = None
        # Specifies how the provisioned Cloud PC will be joined to Azure AD. If you choose the hybridAzureADJoin type, only provide a value for the onPremisesConnectionId property and leave regionName as empty. If you choose the azureADJoin type, provide a value for either onPremisesConnectionId or regionName. The possible values are: azureADJoin, hybridAzureADJoin, unknownFutureValue.
        self._type: Optional[cloud_pc_domain_join_type.CloudPcDomainJoinType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcDomainJoinConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcDomainJoinConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcDomainJoinConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "on_premises_connection_id": lambda n : setattr(self, 'on_premises_connection_id', n.get_str_value()),
            "region_group": lambda n : setattr(self, 'region_group', n.get_enum_value(cloud_pc_region_group.CloudPcRegionGroup)),
            "region_name": lambda n : setattr(self, 'region_name', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(cloud_pc_domain_join_type.CloudPcDomainJoinType)),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def on_premises_connection_id(self,) -> Optional[str]:
        """
        Gets the onPremisesConnectionId property value. The Azure network connection ID that matches the virtual network IT admins want the provisioning policy to use when they create Cloud PCs. You can use this property in both domain join types: Azure AD joined or Hybrid Azure AD joined. If you enter an onPremisesConnectionId, leave regionName as empty.
        Returns: Optional[str]
        """
        return self._on_premises_connection_id
    
    @on_premises_connection_id.setter
    def on_premises_connection_id(self,value: Optional[str] = None) -> None:
        """
        Sets the onPremisesConnectionId property value. The Azure network connection ID that matches the virtual network IT admins want the provisioning policy to use when they create Cloud PCs. You can use this property in both domain join types: Azure AD joined or Hybrid Azure AD joined. If you enter an onPremisesConnectionId, leave regionName as empty.
        Args:
            value: Value to set for the onPremisesConnectionId property.
        """
        self._on_premises_connection_id = value
    
    @property
    def region_group(self,) -> Optional[cloud_pc_region_group.CloudPcRegionGroup]:
        """
        Gets the regionGroup property value. The regionGroup property
        Returns: Optional[cloud_pc_region_group.CloudPcRegionGroup]
        """
        return self._region_group
    
    @region_group.setter
    def region_group(self,value: Optional[cloud_pc_region_group.CloudPcRegionGroup] = None) -> None:
        """
        Sets the regionGroup property value. The regionGroup property
        Args:
            value: Value to set for the regionGroup property.
        """
        self._region_group = value
    
    @property
    def region_name(self,) -> Optional[str]:
        """
        Gets the regionName property value. The supported Azure region where the IT admin wants the provisioning policy to create Cloud PCs. The underlying virtual network will be created and managed by the Windows 365 service. This can only be entered if the IT admin chooses Azure AD joined as the domain join type. If you enter a regionName, leave onPremisesConnectionId as empty.
        Returns: Optional[str]
        """
        return self._region_name
    
    @region_name.setter
    def region_name(self,value: Optional[str] = None) -> None:
        """
        Sets the regionName property value. The supported Azure region where the IT admin wants the provisioning policy to create Cloud PCs. The underlying virtual network will be created and managed by the Windows 365 service. This can only be entered if the IT admin chooses Azure AD joined as the domain join type. If you enter a regionName, leave onPremisesConnectionId as empty.
        Args:
            value: Value to set for the regionName property.
        """
        self._region_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("onPremisesConnectionId", self.on_premises_connection_id)
        writer.write_enum_value("regionGroup", self.region_group)
        writer.write_str_value("regionName", self.region_name)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def type(self,) -> Optional[cloud_pc_domain_join_type.CloudPcDomainJoinType]:
        """
        Gets the type property value. Specifies how the provisioned Cloud PC will be joined to Azure AD. If you choose the hybridAzureADJoin type, only provide a value for the onPremisesConnectionId property and leave regionName as empty. If you choose the azureADJoin type, provide a value for either onPremisesConnectionId or regionName. The possible values are: azureADJoin, hybridAzureADJoin, unknownFutureValue.
        Returns: Optional[cloud_pc_domain_join_type.CloudPcDomainJoinType]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[cloud_pc_domain_join_type.CloudPcDomainJoinType] = None) -> None:
        """
        Sets the type property value. Specifies how the provisioned Cloud PC will be joined to Azure AD. If you choose the hybridAzureADJoin type, only provide a value for the onPremisesConnectionId property and leave regionName as empty. If you choose the azureADJoin type, provide a value for either onPremisesConnectionId or regionName. The possible values are: azureADJoin, hybridAzureADJoin, unknownFutureValue.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

