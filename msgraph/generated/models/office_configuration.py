from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

office_client_checkin_status = lazy_import('msgraph.generated.models.office_client_checkin_status')
office_client_configuration = lazy_import('msgraph.generated.models.office_client_configuration')
office_user_checkin_summary = lazy_import('msgraph.generated.models.office_user_checkin_summary')

class OfficeConfiguration(AdditionalDataHolder, Parsable):
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
    
    @property
    def client_configurations(self,) -> Optional[List[office_client_configuration.OfficeClientConfiguration]]:
        """
        Gets the clientConfigurations property value. List of office Client configuration.
        Returns: Optional[List[office_client_configuration.OfficeClientConfiguration]]
        """
        return self._client_configurations
    
    @client_configurations.setter
    def client_configurations(self,value: Optional[List[office_client_configuration.OfficeClientConfiguration]] = None) -> None:
        """
        Sets the clientConfigurations property value. List of office Client configuration.
        Args:
            value: Value to set for the clientConfigurations property.
        """
        self._client_configurations = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new OfficeConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # List of office Client configuration.
        self._client_configurations: Optional[List[office_client_configuration.OfficeClientConfiguration]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # List of office Client check-in status.
        self._tenant_checkin_statuses: Optional[List[office_client_checkin_status.OfficeClientCheckinStatus]] = None
        # Entity that describes tenant check-in statues
        self._tenant_user_checkin_summary: Optional[office_user_checkin_summary.OfficeUserCheckinSummary] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OfficeConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OfficeConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OfficeConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "client_configurations": lambda n : setattr(self, 'client_configurations', n.get_collection_of_object_values(office_client_configuration.OfficeClientConfiguration)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "tenant_checkin_statuses": lambda n : setattr(self, 'tenant_checkin_statuses', n.get_collection_of_object_values(office_client_checkin_status.OfficeClientCheckinStatus)),
            "tenant_user_checkin_summary": lambda n : setattr(self, 'tenant_user_checkin_summary', n.get_object_value(office_user_checkin_summary.OfficeUserCheckinSummary)),
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("clientConfigurations", self.client_configurations)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("tenantCheckinStatuses", self.tenant_checkin_statuses)
        writer.write_object_value("tenantUserCheckinSummary", self.tenant_user_checkin_summary)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def tenant_checkin_statuses(self,) -> Optional[List[office_client_checkin_status.OfficeClientCheckinStatus]]:
        """
        Gets the tenantCheckinStatuses property value. List of office Client check-in status.
        Returns: Optional[List[office_client_checkin_status.OfficeClientCheckinStatus]]
        """
        return self._tenant_checkin_statuses
    
    @tenant_checkin_statuses.setter
    def tenant_checkin_statuses(self,value: Optional[List[office_client_checkin_status.OfficeClientCheckinStatus]] = None) -> None:
        """
        Sets the tenantCheckinStatuses property value. List of office Client check-in status.
        Args:
            value: Value to set for the tenantCheckinStatuses property.
        """
        self._tenant_checkin_statuses = value
    
    @property
    def tenant_user_checkin_summary(self,) -> Optional[office_user_checkin_summary.OfficeUserCheckinSummary]:
        """
        Gets the tenantUserCheckinSummary property value. Entity that describes tenant check-in statues
        Returns: Optional[office_user_checkin_summary.OfficeUserCheckinSummary]
        """
        return self._tenant_user_checkin_summary
    
    @tenant_user_checkin_summary.setter
    def tenant_user_checkin_summary(self,value: Optional[office_user_checkin_summary.OfficeUserCheckinSummary] = None) -> None:
        """
        Sets the tenantUserCheckinSummary property value. Entity that describes tenant check-in statues
        Args:
            value: Value to set for the tenantUserCheckinSummary property.
        """
        self._tenant_user_checkin_summary = value
    

