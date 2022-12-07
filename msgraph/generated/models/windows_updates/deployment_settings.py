from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

monitoring_settings = lazy_import('msgraph.generated.models.windows_updates.monitoring_settings')
rollout_settings = lazy_import('msgraph.generated.models.windows_updates.rollout_settings')
safeguard_settings = lazy_import('msgraph.generated.models.windows_updates.safeguard_settings')

class DeploymentSettings(AdditionalDataHolder, Parsable):
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
        Instantiates a new deploymentSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Settings governing conditions to monitor and automated actions to take.
        self._monitoring: Optional[monitoring_settings.MonitoringSettings] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Settings governing how the content is rolled out.
        self._rollout: Optional[rollout_settings.RolloutSettings] = None
        # Settings governing safeguard holds on offering content.
        self._safeguard: Optional[safeguard_settings.SafeguardSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeploymentSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeploymentSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeploymentSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "monitoring": lambda n : setattr(self, 'monitoring', n.get_object_value(monitoring_settings.MonitoringSettings)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "rollout": lambda n : setattr(self, 'rollout', n.get_object_value(rollout_settings.RolloutSettings)),
            "safeguard": lambda n : setattr(self, 'safeguard', n.get_object_value(safeguard_settings.SafeguardSettings)),
        }
        return fields
    
    @property
    def monitoring(self,) -> Optional[monitoring_settings.MonitoringSettings]:
        """
        Gets the monitoring property value. Settings governing conditions to monitor and automated actions to take.
        Returns: Optional[monitoring_settings.MonitoringSettings]
        """
        return self._monitoring
    
    @monitoring.setter
    def monitoring(self,value: Optional[monitoring_settings.MonitoringSettings] = None) -> None:
        """
        Sets the monitoring property value. Settings governing conditions to monitor and automated actions to take.
        Args:
            value: Value to set for the monitoring property.
        """
        self._monitoring = value
    
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
    def rollout(self,) -> Optional[rollout_settings.RolloutSettings]:
        """
        Gets the rollout property value. Settings governing how the content is rolled out.
        Returns: Optional[rollout_settings.RolloutSettings]
        """
        return self._rollout
    
    @rollout.setter
    def rollout(self,value: Optional[rollout_settings.RolloutSettings] = None) -> None:
        """
        Sets the rollout property value. Settings governing how the content is rolled out.
        Args:
            value: Value to set for the rollout property.
        """
        self._rollout = value
    
    @property
    def safeguard(self,) -> Optional[safeguard_settings.SafeguardSettings]:
        """
        Gets the safeguard property value. Settings governing safeguard holds on offering content.
        Returns: Optional[safeguard_settings.SafeguardSettings]
        """
        return self._safeguard
    
    @safeguard.setter
    def safeguard(self,value: Optional[safeguard_settings.SafeguardSettings] = None) -> None:
        """
        Sets the safeguard property value. Settings governing safeguard holds on offering content.
        Args:
            value: Value to set for the safeguard property.
        """
        self._safeguard = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("monitoring", self.monitoring)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("rollout", self.rollout)
        writer.write_object_value("safeguard", self.safeguard)
        writer.write_additional_data_value(self.additional_data)
    

